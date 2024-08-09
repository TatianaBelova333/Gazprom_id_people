from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets

from apps.projects.models import ProgressStatus
from api.serializers import ProgressStatusSerializer


@extend_schema(tags=['Project/component/service editing'])
@extend_schema_view(
    list=extend_schema(summary='List all progress statuses'),
)
class ProgressStatusListViewset(mixins.ListModelMixin,
                                viewsets.GenericViewSet):
    '''
    list:
    Return a list of all existing progress statuses.

    '''
    queryset = ProgressStatus.objects.all()
    serializer_class = ProgressStatusSerializer
    pagination_class = None
