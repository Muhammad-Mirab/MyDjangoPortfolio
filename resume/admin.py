from django.contrib import admin

# Register your models here.
from .models import universityAndEducation, experiences, skills

admin.site.register(skills)
admin.site.register(experiences)
admin.site.register(universityAndEducation)