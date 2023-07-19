from django.shortcuts import render
from User.models import UserProfile,Scripts

# Create your views here.

import openai
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
import json


import openai
from nolan import settings

#openai.organization = "org-chuck-norris-kernel"
openai.api_key = settings.ChatGPTKey



def Script(request):
  return render(request,"Script.html")
def generate_script(title, plot, genre):
    if openai.api_key == "":
        print("No API key.")
        return "No API key."

    script_metadata = ""
    script_metadata += f"Title: {title}\n\n"
    script_metadata += "Plot:\n"
    script_metadata += f"{plot}\n\n"
    script_metadata += f"Genre: {genre}\n\n"

    request = """
    This is a script generation application.
    """ + script_metadata + """
    The script should contain 2 scenes and a list of characters.
    Do provide the complete dialogues and detailed descriptions.
    Reply in JSON format: {
        "script": "Script content",
        "Characters": "List of characters"
    }
    The response should only contain this JSON object.
    If needed, you should use basic screenplay formatting.
    """
    print("IN GENERATE ", request)

    return query(request)

def query(request):
    # Call OpenAI API to generate the script
    print("IN query")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.2
    )
    print(response)

    if response.choices:
        script = response.choices[0].text.strip().replace('\n', '\n\n')
        print("SCRIPT",script)
        return script
    else:
        print("FAILED  FOR SOME REASONs", response.choices)
        return "Script generation failed."

#openai.api_key = "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"
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
      print("FORM IS VALID")
      title=form.cleaned_data['title']
      plot=form.cleaned_data['Plot']
      genre=form.cleaned_data['genres']
      print(form.cleaned_data['title'])
      DATA=generate_script(title, plot, genre)
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