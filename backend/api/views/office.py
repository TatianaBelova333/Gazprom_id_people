from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from apps.company_structure.models import CompanyOffice
from api.serializers import OfficeSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(summary='List all company offices'),
)
class OfficeReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all company offices.

    retrieve:
    Return a single company office.

    '''
    queryset = CompanyOffice.objects.all()
    serializer_class = OfficeSerializer
    pagination_class = None
