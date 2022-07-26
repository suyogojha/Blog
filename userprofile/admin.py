from django.contrib import admin
from .models import profile
# Register your models here.

@admin.register(profile)
class UserprofileAdmin(admin.ModelAdmin):
    list_display = ("User","first_name", "last_name", "address", "contact")