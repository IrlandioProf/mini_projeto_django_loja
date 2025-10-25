from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include("apps.clientes.urls")),
    path("api/", include("apps.clientes.api_urls")),
    path("", include("apps.clientes.urls")),  # home provisória
]
