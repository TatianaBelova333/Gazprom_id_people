from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets

from apps.staff.models import Skill
from api.serializers import SkillSerializer


@extend_schema(tags=["Employee's Profile editing"])
@extend_schema_view(
    list=extend_schema(summary='List all employee skills'),
)
class SkillReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    list:
    Return a list of all existing employee skills.

    retrieve:
    Return a single skill.

    '''
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
