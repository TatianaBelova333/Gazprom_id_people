import base64

from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
from djoser.serializers import UserSerializer
from rest_framework import serializers

from apps.staff.models import EmployeeStatus, SavedContact, Skill
from apps.projects.models import Project


Employee = get_user_model()


class EmployeeStatusSerializer(serializers.ModelSerializer):
    '''Serializer for Employee's work status.'''

    class Meta:
        model = EmployeeStatus
        fields = ('id', 'name', 'color')


class SkillSerializer(serializers.ModelSerializer):
    '''Serializer for Employee's skills.'''

    class Meta:
        model = Skill
        fields = ('id', 'name', 'color')


class PositionSerializer(serializers.ModelSerializer):
    '''Serializer for Employee's position.'''

    class Meta:
        model = Skill
        fields = ('id', 'name')


class UnitSerializer(serializers.ModelSerializer):
    '''Serializer for Employee's unit.'''

    class Meta:
        model = Skill
        fields = ('id', 'name')


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class ProjectNameSerializer(serializers.ModelSerializer):
    '''Serialiser for listing employee projects in the employee catalogue.'''

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
        )


class LeaderSerializer(serializers.ModelSerializer):
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
    '''Serialiser for a list of all Employees.'''
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


class EmployeeSerializer(UserSerializer):
    '''Serialiser for Employee's profile.'''
    is_saved_contact = serializers.SerializerMethodField()
    office = serializers.StringRelatedField(read_only=True)
    status = EmployeeStatusSerializer()
    skills = SkillSerializer(many=True, read_only=True)
    position = PositionSerializer()
    unit = UnitSerializer()
    leader = serializers.SerializerMethodField()
    image = Base64ImageField(required=False, allow_null=True)
    leader = serializers.SerializerMethodField()

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
            'office',
            'status',
            'skills',
            'image',
            'ms_teams',
            'is_saved_contact',
            'employment_type',
            'office',
            'position',
            'unit',
            'leader',
        )

    def _get_current_user(self):
        request = self.context.get('request')
        if request:
            return request.user

    def get_is_saved_contact(self, obj):
        '''
        Return True of the obj in the request user's saved contacts.
        False, otherwise.

        '''
        request_user = self._get_current_user()
        if request_user:
            return (request_user.is_authenticated
                    and SavedContact.objects.filter(
                        employee=request_user,
                        contact=obj
                    ).exists())
        return False

    def get_leader(self, obj) -> LeaderSerializer:
        '''Return the employee's manager or None.'''
        request_user = self._get_current_user()

        if request_user:
            # if employee belongs to a certain unit,
            # their leader is the team lead
            if (obj.unit is not None
                    and obj.unit.team is not None):

                team_lead = obj.unit.team.team_lead
                if team_lead:
                    return LeaderSerializer(obj.unit.team.team_lead) if team_lead else None
            # if the employee is a team lead,
            # their leader is the department head
            if hasattr(obj, 'team'):
                team = obj.team
                if team.department is not None:
                    head = team.department.head
                    return LeaderSerializer(head) if head else None

            # if the employee is a department head,
            # their leader is the product_owner
            if hasattr(obj, 'department'):
                product_owner = obj.department.product_owner
                return LeaderSerializer(product_owner)
