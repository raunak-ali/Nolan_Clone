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

# Create your views here.
def login(request):
  print(request.user.email)
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

    return render(request, "Home.html")
  else:
    return render(request, "login.html") 



  
  
  return render(request, "login.html")


def home(request):
  return render(request, "home.html")
# Create your views here.
