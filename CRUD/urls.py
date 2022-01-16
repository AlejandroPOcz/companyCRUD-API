"""CRUD app Url's"""

# Django
from django.urls import path

# Flink
from . import views

urlpatterns = [
    path(
        '',
        views.apiOverview,
        name='api-overview'
    ),
    path(
        'company-api/',
        views.companyList,
        name='company-list'
    ),
    path(
        'company-api/detail/<str:id>',
        views.companyDetail,
        name='company-detail'
    ),
    path(
        'company-api/create/',
        views.companyCreate,
        name='company-create'
    ),
    path(
        'company-api/update/<str:id>',
        views.companyUpdate,
        name='company-update'
    ),
    path(
        'company-api/delete/<str:id>',
        views.companyDelete,
        name='company-delete'
    ),
    # path(
    #     'company-api/<str:company>',
    #     views.tryingAPI,
    #     name='trying-api'
    # ),
]
