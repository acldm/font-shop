from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(req):
  
  if req.method == 'POST':
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
      login(req, user)
      return redirect(reverse("index"))
  return render(req, 'common/login.html')

def index(req):
  return render(req, 'common/index.html')