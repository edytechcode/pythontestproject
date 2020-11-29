from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projecTs = Project.objects.all()[:3]
    return render(request, 'portfolio/home.html', {'proj': projecTs})

def contact(request):
    return render(request, 'portfolio/contact.html')


