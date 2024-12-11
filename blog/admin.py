from django.contrib import admin
from .models import Article, Category, Comment,Message  # New


class FilterByTitle(admin.SimpleListFilter):
    title = " کلید های پر تکرار "
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
                ("titanic","TINTANIC"),
        )
    def queryset(self, request, queryset):
        if self.value() :
            return queryset.filter(title__icontains =self.value())

class CommentInline(admin.TabularInline):
    model = Comment



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","body","status","show_image")
    list_editable = ("body",)
    list_filter = ("status",FilterByTitle)
    search_fields = ("title","body")
    fields = ("body","status","title","category","author")
    inlines = [CommentInline]


admin.site.register(Category)
# admin.site.register(New)
admin.site.register(Comment)
admin.site.register(Message)