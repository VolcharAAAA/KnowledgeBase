from django.contrib.auth import login
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def signup(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid(): #True of false
            user = form.save()
            login(request, user)
            return redirect("post_list")   
    else:
        form = SignUpForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)