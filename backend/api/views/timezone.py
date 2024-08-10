from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from apps.staff.models import EmployeeTimeZone
from api.serializers import EmployeeTimeZoneSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(summary='List all timezones'),
)
class TimeZoneReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all timezones for employee's profile.

    retrieve:
    Return a single timezone.

    '''
    queryset = EmployeeTimeZone.objects.all()
    serializer_class = EmployeeTimeZoneSerializer
    pagination_class = None
