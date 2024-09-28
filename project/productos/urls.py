from django.urls import path

from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.index, name='index'),
    # path(
    #     'productocategoria/list/',
    #     views.productocategoria_list,
    #     name='productocategoria_list',
    # ),
    path(
        'productocategoria/list/',
        views.ProductoCategoriaList.as_view(),
        name='productocategoria_list',
    ),
    # path(
    #     'productocategoria/create/',
    #     views.productocategoria_create,
    #     name='productocategoria_create',
    # ),
    path(
        'productocategoria/create/',
        views.ProductoCategoriaCreate.as_view(),
        name='productocategoria_create',
    ),
    # path(
    #     'productocategoria/detail/<int:pk>',
    #     views.productocategoria_detail,
    #     name='productocategoria_detail',
    # ),
    path(
        'productocategoria/detail/<int:pk>',
        views.ProductoCategoriaDetail.as_view(),
        name='productocategoria_detail',
    ),
    # path(
    #     'productocategoria/update/<int:pk>',
    #     views.productocategoria_update,
    #     name='productocategoria_update',
    # ),
    path(
        'productocategoria/update/<int:pk>',
        views.ProductoCategoriaUpdate.as_view(),
        name='productocategoria_update',
    ),
    path(
        'productocategoria/delete/<int:pk>',
        views.ProductoCategoriaDelete.as_view(),
        name='productocategoria_delete',
    ),
]
