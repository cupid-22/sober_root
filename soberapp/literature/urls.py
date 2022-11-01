from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import LiteratureViewSet, LiteratureSubSectionViewSet, LiteratureSubSectionDetailViewSet

router = ExtendedSimpleRouter()

router.register("subsection", LiteratureSubSectionDetailViewSet)

re_router = router.register("", LiteratureViewSet)
re_router.register(
    "subsection", LiteratureSubSectionViewSet, basename="subsection",
    parents_query_lookups=['literature']
)

urlpatterns = []
urlpatterns += router.urls
