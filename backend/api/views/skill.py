from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets

from apps.staff.models import Skill
from api.serializers import SkillSerializer


@extend_schema(tags=["Employee's Profile Editing"])
@extend_schema_view(
    list=extend_schema(summary='List all employee skills'),
)
class SkillListViewset(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    '''
    list:
    Return a list of all existing employee skills.

    '''
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    pagination_class = None
