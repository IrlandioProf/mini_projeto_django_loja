from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.ClienteList.as_view(), name='lista'),
    path('novo/', views.ClienteCreate.as_view(), name='criar'),
    path('<int:pk>/editar/', views.ClienteUpdate.as_view(), name='editar'),
    path('<int:pk>/excluir/', views.ClienteDelete.as_view(), name='excluir'),
]
