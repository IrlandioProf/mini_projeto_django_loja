from django.contrib import admin
from django.urls import path, include
from apps.clientes.views import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("apps.clientes.urls")),
    path("api/", include("apps.clientes.api_urls")),
    # Home: renderiza template simples em vez de redirecionar
    path("", HomeView.as_view(), name='home'),
]
