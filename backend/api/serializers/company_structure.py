from rest_framework import serializers

from apps.company_structure.models import (
    Company,
    CompanyDepartment,
    CompanyTeam,
    CompanyUnit,
)
from apps.staff.models import Employee


class EmployeeBriefInfoSerializer(serializers.ModelSerializer):
    '''Employee Serializer for the Company Tree Structure.'''
    position = serializers.CharField(source='position.name')

    class Meta:
        model = Employee
        fields = (
            'id',
            'image',
            'employment_type',
            'first_name',
            'last_name',
            'position',
        )


class CompanyUnitSerializer(serializers.ModelSerializer):
    '''Unit(Подразделение) Serializer for the Company Tree Structure.'''
    employees = EmployeeBriefInfoSerializer(many=True)

    class Meta:
        model = CompanyUnit
        fields = (
            'id',
            'name',
            'employees',
        )


class CompanyTeamSerializer(serializers.ModelSerializer):
    '''Team(Отдел) Serializer for the Company Tree Structure.'''
    team_lead = EmployeeBriefInfoSerializer()
    units = CompanyUnitSerializer(many=True)

    class Meta:
        model = CompanyTeam
        fields = (
            'id',
            'name',
            'team_lead',
            'units',
        )


class CompanyDepartmentSerializer(serializers.ModelSerializer):
    '''Department(Департамент) Serializer for the Company Structure.'''
    head = EmployeeBriefInfoSerializer()
    teams = CompanyTeamSerializer(many=True)

    class Meta:
        model = CompanyDepartment
        fields = ('id', 'name', 'head', 'teams')


class CompanyStructureSerializer(serializers.ModelSerializer):
    '''Company(Компания) Serializer for the Company Structure.'''
    director = EmployeeBriefInfoSerializer()
    departments = CompanyDepartmentSerializer(many=True)
    company_name = serializers.CharField(source='name')

    class Meta:
        model = Company
        fields = ('id', 'company_name', 'director', 'departments')
