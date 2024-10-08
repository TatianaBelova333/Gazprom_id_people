from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from apps.staff.models import EmployeeStatus
from api.serializers import EmployeeStatusSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(summary='List all employee statuses'),
)
class EmployeeStatusReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all existing employee statuses.

    retrieve:
    Return a single employee status.

    '''
    queryset = EmployeeStatus.objects.all()
    serializer_class = EmployeeStatusSerializer
    pagination_class = None
