from django.contrib import admin
from .models import Category, Tag, PublishedPost, DraftPost, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class PublishedPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "updated_at",
        "category",
        "version",
    )
    list_filter = ("author", "created_at", "updated_at", "category")
    search_fields = ("title", "author__username", "content")


class DraftPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at", "category")
    list_filter = ("author", "created_at", "updated_at", "category")
    search_fields = ("title", "author__username", "content")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at", "content")
    list_filter = ("author", "created_at", "post")
    search_fields = ("author__username", "content", "post__title")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PublishedPost, PublishedPostAdmin)
admin.site.register(DraftPost, DraftPostAdmin)
admin.site.register(Comment, CommentAdmin)
