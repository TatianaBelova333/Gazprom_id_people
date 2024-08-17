from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.serializers import (
    ComponentCreateUpdateSerializer,
    ComponentDetailSerializer,
    ComponentListSerializer
)
from apps.projects.models import Component


@extend_schema(tags=['Components'])
@extend_schema_view(
    list=extend_schema(summary='List all components for the dropdown.'),
    create=extend_schema(summary='Create a new component.'),
    partial_update=extend_schema(summary='Update a new component.'),
    retrieve=extend_schema(summary='Retrieve a component by pk.'),
)
class ComponentViewSet(viewsets.ModelViewSet):
    '''
    list:
    Return a list of all components.

    retrieve:
    Return component by id.

    '''
    queryset = Component.objects.select_related(
        'status',
        ).prefetch_related(
            'team_members'
        ).exclude(is_archived=True).distinct()
    serializer_class = ComponentListSerializer
    pagination_class = None
    permission_classes = (IsAdminOrReadOnly,)
    http_method_names = ['get', 'post', 'retrieve', 'patch']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ComponentDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return ComponentCreateUpdateSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
