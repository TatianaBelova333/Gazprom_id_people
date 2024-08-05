from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.employee import EmployeeViewSet
from api.views.employee_status import EmployeeStatusViewset

app_name = 'api'
VERSION = 'v1'

router_1 = DefaultRouter()
router_1.register('users', EmployeeViewSet, basename='users')
router_1.register(
    'user_statuses',
    EmployeeStatusViewset,
    basename='user_statuses'
)


urlpatterns = [
    path(f'{VERSION}/', include((router_1.urls))),
    path(f'{VERSION}/auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
