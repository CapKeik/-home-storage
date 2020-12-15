from django.shortcuts import render


def home(request):
    return render(request, 'finance/home.html')


def profile(request):
    return render(request, 'finance/profile.html')
