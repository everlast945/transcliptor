from django.contrib.auth.views import LoginView

# Create your views here.
from django.views.generic import ListView

from users.forms import UserAuthenticationForm
from users.models import User


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True



class UserListView(ListView):
    model = User
