from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from djoser.conf import settings
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view, extend_schema

from apps.staff.models import SavedContact
from apps.projects.models import Project
from api.pagination import EmployeeListPaginationClass
from api.serializers import ProjectMainPageSerializer

Employee = get_user_model()


@extend_schema(tags=["Employee's Profile"])
@extend_schema_view(
    update=extend_schema(exclude=True),
    create=extend_schema(exclude=True),
    partial_update=extend_schema(
        summary='Partially update a user',
    ),
    list=extend_schema(
        summary='List all employees (Справочник)',
    ),
)
class EmployeeViewSet(DjoserUserViewSet):
    '''
    Extends the Djoser UserViewSet.

    Additional endpoints:

    /contacts:
    Add/remove the given user to/from the request user's saved contancts.

    /me/contacts:
    list the current employee's saved contacts.

    '''
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ('skills', 'employment_type', 'projects')
    search_fields = ('first_name', 'last_name', 'middle_name', 'email')
    ordering_fields = ('last_name', 'position')
    pagination_class = EmployeeListPaginationClass
    queryset = Employee.objects.select_related(
        'position',
        'unit__team__team_lead',
        'timezone',
        'status',
        'office',
    ).prefetch_related('skills', 'projects', 'directed_projects').all()

    def get_serializer_class(self):
        if self.action in ('contacts', 'my_contacts'):
            return settings.SERIALIZERS.contacts

        if self.action == 'list':
            return settings.SERIALIZERS.user_list

        if self.request and self.request.method in ('PATCH', 'PUT'):
            return settings.SERIALIZERS.user_update

        return super().get_serializer_class()

    def get_queryset(self):
        current_employee = self.request.user

        if self.action == 'my_contacts':
            return current_employee.contacts.select_related(
                'contact__position'
            ).all()

        if self.action == 'projects':
            queryset = Project.objects.select_related(
                'director', 'status'
            ).prefetch_related(
                'tags', 'team_members',
            ).filter(
                Q(director=current_employee) | Q(team_members=current_employee)
            ).exclude(is_archived=True).distinct()
            return queryset

        return super().get_queryset()

    @extend_schema(
        summary="Get/update the current user's profile",
    )
    @action(['get', 'patch'], detail=False)
    def me(self, request, *args, **kwargs):
        '''The current user's profile.'''
        self.get_object = self.get_instance

        if request.method == 'GET':
            return super().retrieve(request, *args, **kwargs)

        elif request.method == 'PATCH':
            return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Add/delete other users to/from the current user'contacts",
    )
    @action(
        ['post', 'delete'],
        detail=True,
        permission_classes=(IsAuthenticated,)
    )
    def contacts(self, request, *args, **kwargs):
        current_employee = self.get_instance()
        another_employee = self.get_object()
        saved_contact = SavedContact.objects.filter(
            employee=current_employee,
            contact=another_employee
        )
        if request.method == 'POST':
            if current_employee != another_employee:
                if not saved_contact.exists():
                    SavedContact.objects.create(
                        employee=current_employee, contact=another_employee,
                    )
                    serializer = self.get_serializer(
                        saved_contact.first()
                    ).data
                    return Response(
                        status=status.HTTP_201_CREATED,
                        data=serializer,
                    )
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data={
                        'errors': (f'Пользователь {another_employee} уже '
                                   f'есть в сохраненных контактах.'),
                    })
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'errors': ('Текущий пользователь не может '
                               'добавлять самого себя в контакты'),
                })

        elif request.method == 'DELETE':
            if saved_contact.exists():
                saved_contact.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'errors': (f'Пользователя {another_employee} '
                               f'нет в сохраненных контактах')
                    }
                )

    @extend_schema(summary="List the current user's contacts",
                   tags=['Main'])
    @action(['get'],
            detail=False,
            url_path='me/contacts',
            pagination_class=None,
            filter_backends=[])
    def my_contacts(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(summary="List the current user's projects",
                   tags=['Main'])
    @action(['get'],
            detail=False,
            url_path='me/projects',
            pagination_class=None,
            filter_backends=[],
            serializer_class=ProjectMainPageSerializer)
    def projects(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # Deactivate other Djoser endpoints
    @extend_schema(exclude=True)
    @action(['post'], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    @action(['post'], detail=False)
    def activation(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    @action(['post'], detail=False)
    def set_email(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    @action(['post'], detail=False)
    def reset_email(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    @action(['post'], detail=False)
    def reset_email_confirm(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
