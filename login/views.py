from django.shortcuts import render

# Create your views here.
def loginView(request):
    return render(request, 'admin/login.html')