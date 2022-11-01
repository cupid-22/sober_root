from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import LiteratureViewSet, LiteratureSubSectionViewSet

router = ExtendedSimpleRouter()
re_router = router.register("", LiteratureViewSet)
re_router.register("subsection", LiteratureSubSectionViewSet, "subsection", parents_query_lookups=['id'])

urlpatterns = []
urlpatterns += router.urls
