from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path("", include(("about.urls", "about"), namespace="about")),
    path("admin/", admin.site.urls),
    path("resume/", include(("resume.urls", "resume"), namespace="resume")),
    path("gallery/", include(("gallery.urls", "gallery"), namespace="gallery")),
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)