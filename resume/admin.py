from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(skills)
admin.site.register(experiences)
admin.site.register(universityAndEducation)