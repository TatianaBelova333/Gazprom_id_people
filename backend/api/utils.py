from typing import Optional

from django.db.models import Case, F, QuerySet, When

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
