from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserRoles(models.TextChoices):
    USER = "user", 'Пользователь'
    ADMIN = "admin", 'Администратор'


class CustomUserManager(BaseUserManager):
    '''
    User model manager where email is the unique identifier
    for authentication instead of username.
    '''
    def create_user(self, email, role=UserRoles.USER, password=None):
        '''
        Creates and saves a new User with the provided email and password.

        '''
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            role=role,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        '''
        Creates and saves a superuser with the given email and password
        '''
        user = self.create_user(
            email=email,
            password=password,
            role=UserRoles.ADMIN,
        )

        user.save(using=self._db)
        return user
