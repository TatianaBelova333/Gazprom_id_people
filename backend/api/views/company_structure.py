from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from apps.company_structure.models import Company
from api.serializers import CompanyStructureSerializer


@extend_schema(tags=['Company Structure'])
@extend_schema_view(
    list=extend_schema(summary='Retrieve company Structure'),
)
class CompanyStructureViewset(mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    '''Return a Company tree structure.'''

    queryset = Company.objects.select_related(
        'director').prefetch_related(
            'departments__teams__units__employees__position',
        ).all()
    serializer_class = CompanyStructureSerializer
    pagination_class = None
    permission_classes = (AllowAny,)
