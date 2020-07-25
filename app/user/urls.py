from django.urls import path

from user import views


urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("sign-up/", views.UserRegisterView.as_view(), name="sign-up"),
]