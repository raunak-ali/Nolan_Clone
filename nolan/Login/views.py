from django.shortcuts import render
from User.models import UserProfile,Scripts

# Create your views here.


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from User.forms import ScriptForm

# Create your views here.)
def GenerateSceen_play(form):
  print(form.cleaned_data['title'])

def home(request):
  #Legts get the form als  well
  form=ScriptForm()
  if request.method=='POST':
    print("POST")
    form.full_clean() 
    print(form)
    form = ScriptForm(request.POST)
    if form.is_valid():
      
      print(form.cleaned_data['title'])
      GenerateSceen_play(form)
    else:
      #   Form is not valid, handle errors
      print("Erros",form.errors)



  #print(request.user.email)
  #Lets create a User profile after every successfull Login,
  #(Check if the User already exists then login them in ito our profile,
  #Else create a new User Profile and rederict to the Dashboard)
  User=request.user
  if User.is_authenticated:
    #Check if the User already has a UserProfile in our system
    user_exists=UserProfile.objects.filter(email=User.email).exists()
    if user_exists == False:
      email = User.email
      user_profile = UserProfile(user=User, email=email)
      user_profile.save()
      #Create a new UserProfile  of this User
    else:
      Userprof=UserProfile.objects.get(email=User.email)
      print(Userprof)
      #Fetach Data of the existing User
    print(user_exists)

    return render(request, "index.html",context={'User':User,'form':form})
  else:
    return render(request, "index.html") 
  return render(request, "index.html")
# Create your views here.
