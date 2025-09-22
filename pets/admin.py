from django.contrib import admin
from .models import Pet

# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'created_at']
    list_filter = ['species', 'breed', 'created_at']
    search_fields = ['name', 'breed']
    list_per_page = 20

