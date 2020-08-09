from django import forms
from django.contrib.auth import get_user_model


class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput()
    )

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "username", "password"]
        widgets = {"password": forms.PasswordInput()}

    def is_valid(self):
        """Validate input data and check password confirmation"""
        return super().is_valid() and (
            self.cleaned_data.get("password")
            == self.cleaned_data.get("password_confirm")
        )

    def save(self):
        """Create new user instance"""
        self.cleaned_data.pop("password_confirm")
        return get_user_model().objects.create_user(
            username=self.cleaned_data.pop("username"),
            password=self.cleaned_data.pop("password"),
            email=self.cleaned_data.pop("email"),
            **self.cleaned_data
        )
