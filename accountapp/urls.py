from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from accountapp import views
from accountapp.apps import AccountappConfig

app_name = AccountappConfig.name

urlpatterns = [
    # предыдущий  url входа
    # path("login/", views.user_login, name="login"),
    # url-адреса входа выхода
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # url для смены пароля
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy("accountapp:password_change_done")),
        name="password_change",
    ),
    path("password-change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("", views.dashboard, name="dashboard"),
]
