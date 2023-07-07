from django.contrib.auth import views as auth_views
from django.urls import path

from accountapp import views
from accountapp.apps import AccountappConfig

app_name = AccountappConfig.name

urlpatterns = [
    # предыдущий  url входа
    # path("login/", views.user_login, name="login"),
    # url-адреса входа выхода
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.dashboard, name="dashboard"),
]
