from django.contrib import admin
from .models import GymContact

@admin.register(GymContact)
class GymContactAdmin(admin.ModelAdmin):
    list_display = ('company','name', 'email', 'phone', 'message','date')
    list_filter = ['date']
    search_fields = ['message', 'name']
