from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def profile(request):
    return HttpResponseRedirect('/finance/profile')
