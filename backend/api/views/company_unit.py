from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets

from apps.company_structure.models import CompanyUnit
from api.serializers import CompanyUnitBriefInfoSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(
        summary='Return a list of all units(Подразделения) in the company.'
    ),
    retrieve=extend_schema(
        summary='Return a single company unit(Подразделение).'
    ),
)
class CompanyUnitViewset(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all units (Подразделения) in the company.
    Search by the name of the team and filter by company units.

    retrieve:
    Return a single company unit (Подразделение).

    '''
    queryset = CompanyUnit.objects.all()
    serializer_class = CompanyUnitBriefInfoSerializer
    pagination_class = None
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    search_fields = ('name',)
    filterset_fields = ('team',)
