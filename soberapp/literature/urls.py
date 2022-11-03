from rest_framework_extensions.routers import ExtendedSimpleRouter
from .views import LiteratureViewSet, LiteratureSubSectionDetailViewSet

router = ExtendedSimpleRouter()

re_router = (
    router
    .register("", LiteratureViewSet)
    .register(
        "subsection",
        LiteratureSubSectionDetailViewSet,
        basename="subsection",
        parents_query_lookups=['literature'],
    )
)

urlpatterns = []
urlpatterns += router.urls
