from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CompanyStructureViewset,
    CompanyTeamViewset,
    CompanyUnitViewset,
    ComponentViewSet,
    EmployeeStatusReadOnlyViewset,
    EmployeeViewSet,
    OfficeReadOnlyViewset,
    PositionReadOnlyViewSet,
    ProgressStatusReadOnlyViewset,
    ProjectViewSet,
    ServiceViewSet,
    SkillReadOnlyViewSet,
    TagReadOnlyViewSet,
    TimeZoneReadOnlyViewSet,
)

app_name = 'api'
VERSION = 'v1'

router_1 = DefaultRouter()
router_1.register('users', EmployeeViewSet, basename='users')
router_1.register('user_statuses',
                  EmployeeStatusReadOnlyViewset,
                  basename='user_statuses')

router_1.register('skills', SkillReadOnlyViewSet, basename='skills')
router_1.register('progress_statuses',
                  ProgressStatusReadOnlyViewset,
                  basename='progress_statuses')

router_1.register('tags', TagReadOnlyViewSet, basename='tags')
router_1.register('timezones', TimeZoneReadOnlyViewSet, basename='timezones')
router_1.register('positions', PositionReadOnlyViewSet, basename='positions')
router_1.register('offices', OfficeReadOnlyViewset, basename='offices')
router_1.register(
    'structures',
    CompanyStructureViewset,
    basename='structures',
),
router_1.register(
    'company_teams', CompanyTeamViewset, basename='company_teams',
)
router_1.register(
    'company_units', CompanyUnitViewset, basename='company_units',
)

router_1.register(
    'projects', ProjectViewSet, basename='projects',
)
router_1.register(
    'services', ServiceViewSet, basename='services',
)
router_1.register(
    'components', ComponentViewSet, basename='components',
)


urlpatterns = [
    path(f'{VERSION}/', include((router_1.urls))),
    path(f'{VERSION}/auth/', include('djoser.urls.jwt')),
]
