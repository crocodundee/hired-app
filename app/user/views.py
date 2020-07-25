from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView


class UserRegisterView(FormView):
    """Register users view"""

    form_class = UserCreationForm
    success_url = "/"
    template_name = "user/sign-up.html"


class UserLoginView(LoginView):
    """User login view"""

    template_name = "user/login.html"


class UserLogoutView(LogoutView):
    """User logout then login view"""

    template_name = "/logout.html"
    next_page = "user/login"
