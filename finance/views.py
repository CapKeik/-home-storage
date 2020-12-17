from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, User


def home(request):
    user = request.user.id
    return render(request, 'finance/home.html', {})


def profile(response, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        raise Http404("Пользователь не найден")
    if response.user == user:
        cat_lst = Category.objects.filter(user=response.user)
        return render(response, 'finance/profile.html', {'cat_lst': cat_lst})
    return render(response, 'finance/home.html')


def add_category(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        raise Http404("Пользователь не найден")
    cat = Category(user=user, name=request.POST['name'])
    cat.save()
    return HttpResponseRedirect(reverse('finance:profile', args=(user.id,)))


def add_amount(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        raise Http404("Пользователь не найден")
    cat = Category.objects.get(name=request.POST['name'])
    cat.amount += request.POST['count']
    return HttpResponseRedirect(reverse('finance:profile', args=(user.id,)))
