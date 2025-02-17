from .models import sideBarInfo, aboutMe, whatIDo

def about_context(request):
    sideBarInfos = sideBarInfo.objects.all()[:1].get()
    aboutMeText = aboutMe.objects.all()[:1].get()
    whatIDos = whatIDo.objects.all().filter()
    email = sideBarInfos.email.split("@")
    return {
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
        "aboutMeText": aboutMeText.text.replace("🇮🇷", '<span style="transform: rotate(180deg) perspective(0); display: inline-block;">🇭🇺</span>'),
        "whatIDo": whatIDos,
    }