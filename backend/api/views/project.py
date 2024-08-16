from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import filters, viewsets
from rest_framework.decorators import action

from api.permissions import IsAdminOrReadOnly
from api.serializers import (
    ProjectCreateUpdateSerializer,
    ProjectDetailSerializer,
    ProjectListSerializer,
    ProjectNameSerializer,
)
from apps.projects.models import Project


@extend_schema(tags=["Projects"])
@extend_schema_view(
    list=extend_schema(summary='List all projects with detailed info'),
    retrieve=extend_schema(summary='Retrieve project by id'),
    update=extend_schema(summary='Update project by id'),
    projects_list=extend_schema(summary='Project list for a dropdown menu'),
)
class ProjectViewSet(viewsets.ModelViewSet):
    '''
    list:
    Return a list of all projects.
    Search by project name and filter by status.

    retrieve:
    Return a project by pk.

    '''
    queryset = Project.objects.select_related(
        'director__position', 'status',
        ).prefetch_related(
            'team_members__position', 'team_members__unit__team',
        ).exclude(is_archived=True).distinct()
    serializer_class = ProjectListSerializer
    pagination_class = None
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ('name',)
    filterset_fields = ('status',)
    permission_classes = (IsAdminOrReadOnly,)
    http_method_names = ['get', 'post', 'retrieve', 'patch']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        if self.action == 'retrieve':
            return ProjectDetailSerializer
        if self.action in ('create', 'update', 'partial_update'):
            return ProjectCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

    @action(['get'],
            detail=False,
            url_path='short',
            pagination_class=None,
            filter_backends=[],
            serializer_class=ProjectNameSerializer)
    def projects_list(self, request, *args, **kwargs):
        '''
        Return a list of projects and their names for a dropdown list.

        '''
        return self.list(request, *args, **kwargs)

    @action(['patch'],
            detail=False,
            url_path='short',
            pagination_class=None,
            filter_backends=[],
            serializer_class=ProjectNameSerializer)
    def structures(self, request, *args, **kwargs):
        '''
        Update team members for several projects.

        '''
        pass
