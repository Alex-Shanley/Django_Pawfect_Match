from django.contrib import admin
from .models import Submission

# Register your models here.

class SubmissionAdmin( admin.ModelAdmin):
    list_display = ['first_name', 'surname', 'email','created_at', ]
    list_filter = [ 'created_at', 'terms']
    search_fields = ['first_name', 'surname', 'email' ]
    list_per_page = 20
    readonly_fields = ['created_at']