from django.contrib.auth import get_user_model
from djoser.conf import settings
from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.staff.models.contacts import SavedContact

Employee = get_user_model()


class EmployeeViewSet(DjoserUserViewSet):
    '''
    Extends the Djoser UserViewSet.

    Additional endpoints:

    contacts:
    Add/remove the given user to/from the request user's saved contancts.

    my_contacts:
    list the current employee's saved contacts.

    '''
    def get_serializer_class(self):
        if self.action in ('contacts', 'my_contacts'):
            return settings.SERIALIZERS.contacts
        return super().get_serializer_class()

    def get_queryset(self):
        current_employee = self.request.user
        if self.action == 'my_contacts':
            return current_employee.contacts.all()
        return super().get_queryset()

    @action(['post', 'delete'], detail=True)
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
                    serializer = self.get_serializer(saved_contact.first()).data
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

    @action(["get"], detail=False)
    def my_contacts(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
