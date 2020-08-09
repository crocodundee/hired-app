from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

from user.forms import CreateUserForm


class UserRegisterView(SuccessMessageMixin, FormView):
    """Register users view"""

    form_class = CreateUserForm
    success_url = "/"
    template_name = "user/sign-up.html"
    success_message = "Your account was created successfully."

    def form_valid(self, form):
        """Register user if valid data provided and authenticate him"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    """User login view"""

    template_name = "user/login.html"


class UserLogoutView(LogoutView):
    """User logout then login view"""

    template_name = "user/logout.html"
