from rest_framework.routers import DefaultRouter
from .views import SobrietyDateViewSet, UserLoginViewSet

router = DefaultRouter()
router.register("login", UserLoginViewSet, "Login Details")
router.register("sobriety", SobrietyDateViewSet, "Sobriety Details")

urlpatterns = []
urlpatterns += router.urls
