from django.urls import path

from accountapp import views
from accountapp.apps import AccountappConfig

app_name = AccountappConfig.name

urlpatterns = [
    path("login/", views.user_login, name="login"),
]
