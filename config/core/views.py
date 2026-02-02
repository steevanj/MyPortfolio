from django.shortcuts import render
from .models import Profile,Skill,Project
def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    return render(request, 'core/home.html', {
        'profile': profile,
        'skills': skills
    })

def projects(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, 'core/project.html', {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    })


def contact(request):
    profile = Profile.objects.first()
    return render(request, 'core/contact.html', {
        'profile': profile
    })

