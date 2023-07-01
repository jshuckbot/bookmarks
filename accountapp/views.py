from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Authenticated successfully")
                return HttpResponse("Disable account")
        return HttpResponse("Invalid login")

    form = LoginForm()
    return render(request, "accountapp/login.html", {"form": form})
