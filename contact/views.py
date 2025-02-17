from django.shortcuts import render, redirect
from .forms import ContactUsForm

def contactView(request):
    # if request.method == 'POST':
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('contact:successView')
    return render(request, 'contact.html', {'form': form})

def successView(request):
    return render(request, 'success.html')