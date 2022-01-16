""" CRUD app Admin"""

# Django
from django.contrib import admin

# Flink
from .models import Company


@admin.register(Company)
class ElementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'symbol']
    search_fields = ['id', 'name', 'description']
    ordering = ['name']
