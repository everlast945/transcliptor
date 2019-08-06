from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from users.forms import UserAuthenticationForm


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True
