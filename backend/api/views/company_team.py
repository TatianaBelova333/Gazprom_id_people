from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets

from apps.company_structure.models import CompanyTeam
from api.serializers import CompanyTeamBriefInfoSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(
        summary='Return a list of all teams(Отделы) in the company.'
    ),
    retrieve=extend_schema(summary='Return a single company team(Отдел).'),
)
class CompanyTeamViewset(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all teams (отделы) in the company.
    Search by the company team name and filter by company units.

    retrieve:
    Return a single company team (отдел).

    '''
    queryset = CompanyTeam.objects.all()
    serializer_class = CompanyTeamBriefInfoSerializer
    pagination_class = None
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = ('name',)
    filterset_fields = ('units',)
