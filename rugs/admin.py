from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Basic Info", {
            "fields": ("name", "slug", "short_description", "description", "image")
        }),
        ("Category Page Sections", {
            "fields": ("design_character", "why_choose"),
            "description": "Design Character: write one item per line. Why Choose It: write the paragraph shown in that box."
        }),
        ("Publishing", {
            "fields": ("order", "is_active")
        }),
    )
    list_display = ("name", "slug", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "short_description", "description")
    list_filter = ("is_active",)
