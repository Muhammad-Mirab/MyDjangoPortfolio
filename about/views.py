from django.shortcuts import render
from .models import *
from resume.models import *
from gallery.models import *

# Create your views here.
def mainView(request):
    sideBarInfos = sideBarInfo.objects.all()[:1].get()
    aboutMeText = aboutMe.objects.all()[:1].get()
    whatIDos = whatIDo.objects.all().filter()
    universityAndEducations = universityAndEducation.objects.all().filter()
    experience = experiences.objects.all().filter()
    skill = skills.objects.all().filter()
    category = categories.objects.all().filter()
    galleries = gallery.objects.all().order_by("-date")
    email = sideBarInfos.email
    email = email.split("@")
    context = {
        "name": sideBarInfos.name,
        "jobTitle": sideBarInfos.jobTitle,
        "email": email[0],
        "mailProvidor": email[1],
        "phoneNumber": sideBarInfos.phoneNumber,
        "birthday": sideBarInfos.birthday,
        "location": sideBarInfos.location,
        "linkedIn": sideBarInfos.linkedInLink,
        "github": sideBarInfos.githubLink,
        "twitter": sideBarInfos.twitterLink,
        "instagram": sideBarInfos.instagramLink,
        "telegram": sideBarInfos.telegramLink,
        "youtube": sideBarInfos.youtubeLink,
        "buyMeACoffee": sideBarInfos.buyMeACoffeeLink,
        "aboutMeText": aboutMeText.text,
        "whatIDo": whatIDos,
        "universityAndEducation": universityAndEducations,
        "experiences": experience,
        "skills": skill,
        "category": category,
        "gallery": galleries,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
