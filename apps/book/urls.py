from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, SectionViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"sections", SectionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
