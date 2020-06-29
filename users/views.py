from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy

from users.forms import UserAuthenticationForm


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse_lazy('contents:category:list')


