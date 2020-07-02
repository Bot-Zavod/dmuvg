from django.contrib import admin

# Register your models here.
from .models import Article


@admin.register(Article)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('header', 'short_description', 'category')
    ordering = ('pk',)