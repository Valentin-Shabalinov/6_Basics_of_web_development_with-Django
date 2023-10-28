from django.contrib import admin

from post.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content', 'image', 'date_of_creation', 'publication_sign')
