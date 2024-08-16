from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from api.permissions import IsAdminOrReadOnly
from api.serializers import (
    ServiceCreateUpdateSerializer,
    ServiceDetailSerializer,
    ServiceListSerializer
)
from apps.projects.models import Service


@extend_schema(tags=['Services'])
@extend_schema_view(
    list=extend_schema(summary='List all services for the dropdown.'),
    retrieve=extend_schema(summary='Retrieve a single service'),
    update=extend_schema(summary='Update service by id'),
)
class ServiceViewSet(viewsets.ModelViewSet):
    '''ModelVieset for services.'''
    queryset = Service.objects.select_related(
        'status',
        ).prefetch_related(
            'team_members__position', 'team_members__unit__team',
        ).exclude(is_archived=True).distinct()
    serializer_class = ServiceListSerializer
    pagination_class = None
    permission_classes = (IsAdminOrReadOnly,)
    http_method_names = ['get', 'post', 'retrieve', 'patch']

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer

        if self.action == 'retrieve':
            return ServiceDetailSerializer

        if self.action in ('create', 'update', 'partial_update'):
            return ServiceCreateUpdateSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
