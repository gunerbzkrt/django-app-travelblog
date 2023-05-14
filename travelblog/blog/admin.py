from django.contrib import admin
from .models import Post, Region

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_date", "region", "country")
    readonly_fields = ("created_date",)
    list_editable = ("author", "region",)
    search_fields = ("title",)
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)

admin.site.register(Post, PostAdmin)
admin.site.register(Region, RegionAdmin)