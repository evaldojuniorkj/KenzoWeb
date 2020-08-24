from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('novoCliente/', views.novoCliente, name='novoCliente'),
    path('listarCliente/', views.listarCliente, name='listarCliente'),
    path('editarCliente/<int:pk>', views.editarCliente, name='editarCliente'),
    path('removerCliente/<int:pk>', views.removerCliente, name='removerCliente')
]