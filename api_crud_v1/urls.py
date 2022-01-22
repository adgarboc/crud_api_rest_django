from django.urls import path

from api_crud_v1 import views

app_name = 'api_crud_v1'

urlpatterns = [
    path(
        'products/list/',
        views.products_list,
        name='products_list'
    ),
    path(
        'products/detail/<int:pk>/',
        views.products_detail,
        name='products_detail'
    ),
    path(
        'products/create/',
        views.products_create,
        name='products_create'
    ),
    path(
        'products/update/<int:pk>/',
        views.products_update,
        name='products_update'
    ),
    path(
        'products/delete/<int:pk>/',
        views.products_delete,
        name='products_delete'
    ),
]
