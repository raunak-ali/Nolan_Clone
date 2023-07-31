from django.shortcuts import render
from User.models import UserProfile,Scripts
import pandas as pd
# Create your views here.
import re
import json
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
    The script should contain 1 initial scenes and a list of characters.
    Do provide the complete dialogues and detailed descriptions and arrange them into specific the dictionary.
    Reply in json DiCTIONARY format: {
        "script": "Script content",
        "scene_headings":"List of all screen_headings used in the script in proper order",
        "dialogues":"List of all dialogues used in the script along with the charcters  speakking them",
        "scene_breakdown":"Scene breakdown based on scene headings that aligns the elements of 
        the above lists to make a scene making a proper arrangement of the action_lines list elements ,
        dialogues list elements ,and shots  list elements(Use list indexing along with the list names  only)",
        "shots ":"dictionary with scene_headings  as key and the shot as the value",
        "descriptive_lines":"List of all lines that dont fit into the above lists used in the script in proper order",
        "Characters": "List of characters"
    }
    The response should only contain this Dictionary.
    No part of the script should be left out of the dictionary
    you should use basic screenplay formatting.
    """
    print("IN GENERATE ", request)

    return query(request)

def query(request):
    # Call OpenAI API to generate the script
    #print("IN query")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=request,
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.2
    )
    #print(response)

    if response.choices:
        script = response.choices[0].text.strip().replace('\n', '\n\n')
        print("SCRIPT",response)
        return script
    else:
        #print("FAILED  FOR SOME REASONs", response.choices)
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
    #print(form)
    form = ScriptForm(request.POST)
    if form.is_valid():
      print("FORM IS VALID")
      title=form.cleaned_data['title']
      plot=form.cleaned_data['Plot']
      genre=form.cleaned_data['genres']
      print(form.cleaned_data['title'])
      DATA=generate_script(title, plot, genre)
      print(DATA)
      DATA= DATA.replace("\n", " ").replace("  ", "")
      data = json.loads(DATA)
      # Extract the script and characters
      script = data['script']
      #characters = data['Characters']
      #script=script.replace(" ","\n")

      # Print the extracted script and characters
      print("Script:")
      print(script)
      print("Characters:")
      #print(characters)
    

      return render(request,"Script.html",{'form':form,'title':title,'DATA':DATA,'script':script})
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