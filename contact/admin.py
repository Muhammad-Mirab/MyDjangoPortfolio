from django.contrib import admin
from .models import contactUsModel
# Register your models here.
@admin.register(contactUsModel)
class contactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    