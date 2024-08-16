from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from apps.projects.models import ProgressStatus
from api.serializers import ProgressStatusSerializer


@extend_schema(tags=['Tags and progress statuses'])
@extend_schema_view(
    list=extend_schema(summary='List all progress statuses'),
)
class ProgressStatusReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all existing progress statuses.

    retrieve:
    Return a single progress status.

    '''
    queryset = ProgressStatus.objects.all()
    serializer_class = ProgressStatusSerializer
    pagination_class = None
