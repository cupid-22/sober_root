from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = []
urlpatterns += router.urls
