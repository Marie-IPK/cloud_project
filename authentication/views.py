from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def handlesignup(request):
    if request.method=="POST":
        uname=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password1")
        confirmpassword=request.POST.get("password2")
        #print(uname, email, password, confirmpassword)

        if password != confirmpassword:
            messages.warning(request, "Password is incorrect")
            return redirect('/signup')
        
        try: 
            if User.objects.get(username=uname):
                messages.info(request, "Username already exist")
                return redirect('/signup')
        except:
            pass

        try: 
            if User.objects.get(email=email):
                messages.info(request, "Email already use")
                return redirect('/signup')
        except:
            pass
        myuser = User.objects.create_user(uname, email, password)
        myuser.save()
        messages.success(request, "signup success ! Please Login")
        return redirect('/login')

    return render(request, 'signup.html')

def handlelogin(request):
    return render(request, 'login.html')