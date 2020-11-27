from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model  = User
        fields = '__all__'


class LoginForm(AuthenticationForm):
    class Meta:
        model  = User
        fields = '__all__'

