import base64

from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from django.db import transaction
from djoser.serializers import UserSerializer
from djoser.conf import settings
from rest_framework import serializers

from api.serializers.company_team import CompanyTeamBriefInfoSerializer
from api.serializers.company_unit import CompanyUnitBriefInfoSerializer
from api.serializers.office import OfficeSerializer
from api.serializers.position import PositionSerializer
from api.serializers.project import (
    ProjectMainPageSerializer,
    ProjectNameSerializer,
)
from api.serializers.skill import SkillSerializer
from api.serializers.timezone import EmployeeTimeZoneSerializer
from apps.staff.models import EmployeeStatus, SavedContact

Employee = get_user_model()


class EmployeeStatusSerializer(serializers.ModelSerializer):
    '''Serializer for Employee's work status.'''

    class Meta:
        model = EmployeeStatus
        fields = ('id', 'name', 'color')


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'last_name',
            'first_name',
            'image',
            'employment_type',
        )


class EmployeeListSerializer(UserSerializer):
    '''Serialiser for listing all Employees.'''
    skills = SkillSerializer(many=True, read_only=True)
    full_name = serializers.CharField(source='get_full_name')
    position = serializers.StringRelatedField()
    projects = ProjectNameSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'image',
            'employment_type',
            'position',
            'skills',
            'projects',
        )


class EmployeeDetailSerializer(UserSerializer):
    '''Serialiser for retrieving Employee's profile.'''
    is_saved_contact = serializers.SerializerMethodField()
    image = Base64ImageField(required=False, allow_null=True)
    manager = serializers.SerializerMethodField()
    employment_type = serializers.ChoiceField(
        choices=Employee.EmployementTypes
    )
    company_team = serializers.SerializerMethodField()
    office = OfficeSerializer()
    position = PositionSerializer()
    status = EmployeeStatusSerializer()
    unit = CompanyUnitBriefInfoSerializer()
    skills = SkillSerializer(many=True)
    timezone = EmployeeTimeZoneSerializer()
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'about_me',
            'phone_number',
            'email',
            'status',
            'skills',
            'image',
            'ms_teams',
            'is_saved_contact',
            'employment_type',
            'office',
            'position',
            'timezone',
            'unit',
            'company_team',
            'manager',
            'projects',
        )
        read_only_fields = (settings.LOGIN_FIELD, 'id', 'team')

    def _get_current_user(self):
        request = self.context.get('request')
        if request:
            return request.user

    def get_projects(self, employee) -> ProjectMainPageSerializer:
        '''
        Return all employee projects as a team member and director.

        '''
        queryset = employee.projects.all() | employee.directed_projects.all()
        all_projects = queryset.select_related(
                'director', 'status'
            ).prefetch_related(
                'tags', 'team_members',
            ).exclude(is_archived=True).distinct()
        return ProjectMainPageSerializer(all_projects, many=True).data

    def get_is_saved_contact(self, employee) -> bool:
        '''
        Return True of the employee is in the request user's saved contacts.
        False, otherwise.

        '''
        request_user = self._get_current_user()
        if request_user:
            return (request_user.is_authenticated
                    and SavedContact.objects.filter(
                        employee=request_user,
                        contact=employee,
                    ).exists())
        return False

    def get_manager(self, employee) -> ManagerSerializer:
        '''Return the employee's manager or None.'''
        # if employee belongs to a certain unit,
        # their manager is the team lead
        unit = employee.unit
        if unit is not None and unit.team is not None:
            team_lead = employee.unit.team.team_lead
            if team_lead:
                return ManagerSerializer(team_lead).data

        # if employee is a team lead,
        # their manager is the department head
        if hasattr(employee, 'team'):
            team = employee.team
            if team.department is not None:
                head = team.department.head
                if head:
                    return ManagerSerializer(head).data

        # if the employee is a department head,
        # their manager is the company director
        if hasattr(employee, 'department'):
            company_director = employee.department.company.director
            if company_director:
                return ManagerSerializer(company_director).data

    def get_company_team(self, employee) -> CompanyTeamBriefInfoSerializer:
        '''Return employee company team (Отдел).'''
        unit = employee.unit
        if unit is not None:
            return CompanyTeamBriefInfoSerializer(unit.team).data

        if hasattr(employee, 'team'):
            return CompanyTeamBriefInfoSerializer(employee.team).data


class EmployeeUpdateSerializer(UserSerializer):
    '''Serialiser for updating Employee's profile.'''
    image = Base64ImageField(required=False, allow_null=True)
    employment_type = serializers.ChoiceField(
        choices=Employee.EmployementTypes
    )
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'birthday',
            'about_me',
            'phone_number',
            'status',
            'skills',
            'image',
            'employment_type',
            'office',
            'position',
            'timezone',
            'unit',
            'team',
        )
        read_only_fields = (settings.LOGIN_FIELD, 'id')

    def _get_current_user(self):
        request = self.context.get('request')
        if request:
            return request.user

    @transaction.atomic
    def update(self, employee, validated_data):
        skills = validated_data.pop('skills', None)
        unit = validated_data.pop('unit', None)
        team = validated_data.pop('team', None)

        employee = super().update(employee, validated_data)
        # если пользователь меняет unit(подразделение),
        # то поле team(отдел) игнорируется и подтягивается из базы данных
        if unit is not None:
            employee.unit = unit

        # при выборе отдела(team) пользователь становится его руководилем,
        # поэтому осуществляется проверка текущего руководителя отдела
        elif team is not None:
            current_team_lead = team.team_lead
            if current_team_lead is None:
                employee.team = team
            else:
                raise serializers.ValidationError(
                    (f'У отдела {team} уже есть '
                     f'руководитель {current_team_lead}.')
                )

        if skills:
            employee.skills.clear()
            employee.skills.add(*skills)

        employee.save()
        return employee

    def to_representation(self, employee) -> EmployeeDetailSerializer:
        return EmployeeDetailSerializer(employee).data


class TeamMemberSerializer(serializers.ModelSerializer):
    '''
    Serializer for team members of projects, services and components.

    '''
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'image',
            'last_name',
            'first_name',
            'employment_type',
            'position',
        )
