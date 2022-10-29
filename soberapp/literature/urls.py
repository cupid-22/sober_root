from rest_framework.routers import DefaultRouter
from .views import LiteratureViewSet

router = DefaultRouter()
router.register("", LiteratureViewSet)

urlpatterns = []
urlpatterns += router.urls
