from rest_framework.routers import DefaultRouter
from .api import ClienteViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')

urlpatterns = router.urls
