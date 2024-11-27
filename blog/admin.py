from django.contrib import admin
from .models import Article, Category, Comment  # New

admin.site.register(Article)
admin.site.register(Category)
# admin.site.register(New)
admin.site.register(Comment)