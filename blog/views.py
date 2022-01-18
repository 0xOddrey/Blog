from PIL.Image import new
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, FormView, TemplateView, DetailView, ListView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AdminPasswordChangeForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import FormMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import datetime
import base64
from .models import *
import json 
import requests

# Create your views here.
#Homepage Landing Page
def Homepage(request):
    
    return render(request, "index.html", {})