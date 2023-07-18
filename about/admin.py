from django.contrib import admin
from .models import *
# Register your models here.

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "photo"]

admin.site.register(aboutMe)
admin.site.register(whatIDo, imageAdmin)
admin.site.register(sideBarInfo)