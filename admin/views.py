from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin import site

# Create your views here.
def adminView(request):
    @login_required(login_url='/login/')
    def adminView(request):
        return render(request, 'admin/home.html', {'site': site})