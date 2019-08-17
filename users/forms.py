from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class UserAuthenticationForm(AuthenticationForm):
    """
    Форма логина
    """


    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].widget.attrs.setdefault('class', '')
        self.fields['username'].widget.attrs['class'] += ' form-control'
        self.fields['password'].widget.attrs.setdefault('class', '')
        self.fields['password'].widget.attrs['class'] += ' form-control'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # todo: Нужно будет убрать создание пользователя
        if username is not None and password:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create(username=username, password=password)
                user.set_password(password)
                user.save()

            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


