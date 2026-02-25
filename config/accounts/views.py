from django.shortcuts import render
def signup(request):
    return render(request, 'accounts/signup.html')
def signin(request):
    return render(request, 'accounts/signin.html')
def signout(request):
   pass
# Create your views here.
