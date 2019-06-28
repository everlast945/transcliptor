from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from users.forms import UserAuthenticationForm


class UserLoginView(LoginView):
    form_class = UserAuthenticationForm
    template_name = 'login.html'
    redirect_authenticated_user = True

    # def post(self, request, *args, **kwargs):
    #
    #     form = self.get_form()  # type: AuthenticationForm
    #     if form.is_valid():
    #         user = form.get_user()
    #         # проверка, что у пользователя есть организация
    #         if not user.organization and not (user.is_staff or user.is_superuser):
    #             form.add_error('username',
    #                            mark_safe('Не установлена организация. <br> Обратитесь к администратору системы.'))
    #             return self.form_invalid(form)
    #         # проверка, что у пользователя есть роль
    #         if not user.role and not (user.is_staff or user.is_superuser):
    #             form.add_error('username',
    #                            mark_safe('Не установлена роль. <br> Обратитесь к администратору системы.'))
    #             return self.form_invalid(form)
    #         return self.form_valid(form)
    #     return self.form_invalid(form)

    # def get_success_url(self):
    #     is_out_password = Settings.is_out_password(self.request.user.change_password_date)
    #     if is_out_password:
    #         return reverse_lazy('change-password') + '?next=' + self.request.POST.get('next', '/')
    #     return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            next_url=self.request.GET.get('next', '')
        ))
        return context

    # def get_form_kwargs(self):
    #     x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR') or self.request.META.get('X-Forwarded-For')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = self.request.META.get('REMOTE_ADDR', '')
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update(dict(
    #         ip=ip,
    #     ))
    #     return kwargs
    #
    # def form_valid(self, form):
    #     remember_me = form.cleaned_data.get('remember_me', False)
    #     if not remember_me:
    #         self.request.session.set_expiry(Settings.get_session_expiration_time())
    #     return super().form_valid(form)