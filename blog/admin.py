from django.contrib import admin
from blog.models import Category, Comment, Blog

class CategoryAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)