from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.forms import LoginForm, ProfileEditForm, UserEditForm, UserRegistrationForm
from accountapp.models import Profile


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


@login_required
def dashboard(request):
    return render(request, "accountapp/dashboard.html", {"section": "dashboard"})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # создаем новый объект пользователя
            # пока не сохраняем его
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            # Сохраняем объект пользователя
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "accountapp/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, "accountapp/register.html", {"user_form": user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, "accountapp/edit.html", {"user_form": user_form, "profile_form": profile_form})
