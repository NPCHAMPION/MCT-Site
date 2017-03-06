from django.contrib import admin
from Blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Post, PostAdmin)
