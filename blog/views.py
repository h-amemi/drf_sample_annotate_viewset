from django.db.models import Exists, F, OuterRef
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Comment, DraftPost, PublishedPost, Tag
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    DraftPostSerializer,
    PublishedPostSerializer,
    TagSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PublishedPostViewSet(viewsets.ModelViewSet):
    queryset = PublishedPost.objects.all().prefetch_related("tags")
    serializer_class = PublishedPostSerializer


class DraftPostViewSet(viewsets.ModelViewSet):
    queryset = DraftPost.objects.annotate(
        has_published_post=Exists(PublishedPost.objects.filter(title=OuterRef("title")))
    ).prefetch_related("tags")
    serializer_class = DraftPostSerializer

    @action(detail=True, methods=["post"])
    def approve(self, request, pk=None):
        draft_post = self.get_object()
        published_post, created = PublishedPost.objects.update_or_create(
            title=draft_post.title,
            defaults={
                "content": draft_post.content,
                "author": draft_post.author,
                "category": draft_post.category,
                # Increment the version number by 1 to reflect the new version of the published post
                "version": F("version") + 1,
            },
        )
        published_post.tags.set(draft_post.tags.all())
        return Response({"status": "approved"}, status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
