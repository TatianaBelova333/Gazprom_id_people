from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets

from apps.company_structure.models import Position
from api.serializers import PositionSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(summary='List all employee positions'),
)
class PositionReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all existing employee position.

    retrieve:
    Return a single employee position.

    '''
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
