from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == "POST":
        Username = request.POST['username']
        FirstName = request.POST['fname']
        LastName = request.POST['lname']
        Email = request.POST['email']
        Password = request.POST['password']
        ConfirmPassword = request.POST['ConfirmPassword']

        # conditions about username, password, confirm password
        if len(Username) > 10:
            messages.error(request, "Username must be under 10 ☹")
            return redirect('register')
        if not Username.isalnum():
            messages.error(request, "Username should be number and alphabet ☹")
            return redirect('register')
        if (Password != ConfirmPassword):
            messages.error(request, "Password does not match ☹")
            return redirect('register')

        myUser = User.objects.create_user(Username, Email, Password)
        myUser.first_name = FirstName
        myUser.last_name = LastName
        myUser.save()
        messages.success(request, "Login successful 😀")
        return redirect('HandleLogin')
    template = loader.get_template('register.html')
    return HttpResponse(template.render({}, request))


def HandleLogin(request):
    if request.method == "POST":
        LoginUsername = request.POST['LoginUsername']
        LoginPassword = request.POST['LoginPassword']

        user = authenticate(username=LoginUsername, password=LoginPassword)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "Invalid Username or password ☹")
            return redirect('HandleLogin')

    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def HandleLogout(request):
    logout(request)
    messages.success(request, "It always seems impossible until it's done! 🚀")
    return redirect('HandleLogin')
