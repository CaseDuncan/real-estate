from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        error_class = "errors"

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'last_name','email']
        error_class = "errors"