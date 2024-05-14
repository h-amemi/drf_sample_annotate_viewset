from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    TagViewSet,
    PublishedPostViewSet,
    DraftPostViewSet,
    CommentViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"tags", TagViewSet)
router.register(r"published-posts", PublishedPostViewSet)
router.register(r"draft-posts", DraftPostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
