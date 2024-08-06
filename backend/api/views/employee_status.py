from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets

from apps.staff.models import EmployeeStatus
from api.serializers import EmployeeStatusSerializer


@extend_schema(tags=["Employee's Profile Editing"])
@extend_schema_view(
    list=extend_schema(summary='List all employee statuses'),
)
class EmployeeStatusListViewset(mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    '''
    list:
    Return a list of all existing employee statuses.

    '''
    queryset = EmployeeStatus.objects.all()
    serializer_class = EmployeeStatusSerializer
    pagination_class = None
