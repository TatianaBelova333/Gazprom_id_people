from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'
VERSION = 'v1'

router_1 = DefaultRouter()
# router_1.register("users", UserViewSet, basename="users")


urlpatterns = [
    path(f'{VERSION}/', include((router_1.urls))),
    path(f'{VERSION}/', include('djoser.urls')),
    path(f'{VERSION}/auth/', include('djoser.urls.jwt')),
]
