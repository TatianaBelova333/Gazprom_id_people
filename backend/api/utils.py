from typing import Optional
from datetime import date

from django.db.models import Case, F, QuerySet, When
from rest_framework import serializers

from apps.projects.models.project import Project
from apps.staff.models import Employee
from api.serializers.team_member import TeamMemberSerializer


def get_team_groups(obj):
    '''
    Return project/service/component members grouped by company teams(отделы).

    '''
    team_members: QuerySet[Employee] = obj.team_members.select_related(
         'position', 'unit__team',
         ).annotate(
              company_team=Case(
                When(unit__isnull=False, then=F('unit__team__name')),
                When(team__isnull=False, then=F('team__name')),
                )
        ).all()

    group_by_company_team: dict[str, QuerySet[Employee]] = {}

    for employee in team_members:
        company_team_name: Optional[str] = employee.company_team
        group_by_company_team[company_team_name] = (
            group_by_company_team.get(company_team_name, []) + [employee]
        )

    company_teams: list[dict[str, list[dict]]] = []

    for company_team_name, employees in group_by_company_team.items():
        company_team = {}
        company_team['name'] = company_team_name
        company_team['employees'] = TeamMemberSerializer(
            employees, many=True).data
        company_teams.append(company_team)

    return company_teams


def check_dates_within_project_dates(start_date, end_date, project):
    project_start_date = project.start_date
    project_end_date = project.end_date

    if start_date:
        if project_start_date and start_date < project_start_date:
            raise serializers.ValidationError(
                (f'Дата начала {start_date} не должна быть раньше '
                 f'даты начала проекта {project_start_date}.')
            )
        if project_end_date and start_date > project_end_date:
            raise serializers.ValidationError(
                (f'Дата начала {start_date} не может быть позже '
                 f'даты окончания проекта {project_end_date}.')
            )

    if end_date:
        if project_end_date and end_date > project_end_date:
            raise serializers.ValidationError(
                (f'Дата окончания {end_date} не может быть позже '
                 f'даты окончания проекта {project_end_date}.')
            )
        if project_start_date and end_date < project_start_date:
            raise serializers.ValidationError(
                (f'Дата окончания {end_date} не может быть раньше '
                 f'даты начала проекта {project_start_date}.')
            )


def check_start_date_lt_end_date(
    start_date: Optional[date],
    end_date: Optional[date]
):
    '''Raise ValidationError if the start_date is greater than the end_date.'''

    if (start_date and end_date) and start_date >= end_date:
        raise serializers.ValidationError(
            'Дата начала не может быть позже даты окончания.'
        )


def check_team_members_belong_to_project(
    members: Optional[QuerySet[Employee]],
    project: Project,
):
    '''
    Check that team members of components and services
    belong to the team of the related project.

    '''
    if members:
        project_members = set(project.team_members.all())
        project_director = project.director
        if project_director:
            project_members.add(project_director)

        if not set(members).issubset(project_members):
            raise serializers.ValidationError(
                ('Участники команды должны '
                 'входить в команду проекта.')
            )
