from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets

from apps.projects.models import WorkTag
from api.serializers import WorkTagSerializer


@extend_schema(tags=['Project/component/service editing'])
@extend_schema_view(
    list=extend_schema(summary='List all work tags'),
)
class TagReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all existing tags.

    retrieve:
    Return a single tag.

    '''
    queryset = WorkTag.objects.all()
    serializer_class = WorkTagSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
