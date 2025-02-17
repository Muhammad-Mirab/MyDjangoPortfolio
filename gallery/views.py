from django.shortcuts import render
from .models import categories, gallery

def galleryView(request):
    category = categories.objects.all().filter()
    galleries = gallery.objects.all().order_by("-date")
    context = {
        "category": category,
        "gallery": galleries,
    }
    return render(request, 'gallery.html', context=context)