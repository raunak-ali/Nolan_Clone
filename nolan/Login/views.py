from django.shortcuts import render


# Create your views here.


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  return render(request, "login.html")


def home(request):
  return render(request, "home.html")
# Create your views here.
