from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from django.contrib import messages 

# Create your views here.

def index(request):
    return render(request, 'index.html')


def SignUp(request):
    # Get the post parameters
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('homepage')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('homepage')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('homepage')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('homepage')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user=authenticate(username = loginusername , password = loginpassword )

        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("homepage")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("homepage")
    
    return HttpResponse('404 - Not found')

    # return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('homepage')
    

