from django.shortcuts import render
from .models import universityAndEducation, experiences, skills

def resumeView(request):
    universityAndEducations = universityAndEducation.objects.all().filter()
    experience = experiences.objects.all().filter()
    skill = skills.objects.all().filter()
    context = {
        "universityAndEducation": universityAndEducations,
        "experiences": experience,
        "skills": skill,
    }
    return render(request, 'resume.html', context=context)