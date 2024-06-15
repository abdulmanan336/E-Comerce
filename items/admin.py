from django.contrib import admin
from django.contrib.sessions.models import Session
from . import models
# Register your models here.

admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.Tag)
@admin.register(models.Item)
class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ('title', 'purchase_price', 'sale_price', 'quantity', 'discount')
    search_fields = ["title", "category__title"]
    list_filter = ("purchase_price", "discount")
    ordering = ("title", )
admin.site.register(models.Image)
admin.site.register(models.Stock)
admin.site.register(models.Special)
admin.site.register(Session)
