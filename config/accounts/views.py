from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
def signup(request):
    if request.user.is_authenticated:
        return redirect('orders')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        r_password = request.POST['r_password']
        if password != r_password:
            return render(request, 'accounts/signup.html', {'error':'Passwords do not match'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('signin')
    return render(request, 'accounts/signup.html')
def signin(request):
    if request.user.is_authenticated:
        return redirect('orders')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('orders')
        else:
            return render(request, 'accounts/signin.html', {'errors':'User or password is incorrect'})
    return render(request, 'accounts/signin.html')
def signout(request):
  logout(request)
  return redirect('signin')
# Create your views here.
