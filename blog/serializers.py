from rest_framework import serializers
from .models import Category, Tag, PublishedPost, DraftPost, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PublishedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublishedPost
        fields = "__all__"


class DraftPostSerializer(serializers.ModelSerializer):
    has_published_post = serializers.SerializerMethodField()

    class Meta:
        model = DraftPost
        fields = "__all__"

    def get_has_published_post(self, obj):
        return PublishedPost.objects.filter(title=obj.title).exists()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
