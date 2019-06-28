from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserAuthenticationForm(AuthenticationForm):
    """
    Форма логина
    """

    error_messages = {
        'invalid_login': 'Неверный пароль',
        'inactive': f'Пользователю запрещен доступ в систему, обратитесь в техническую поддержку: ',
    }

    remember_me = forms.BooleanField(required=False, label='Запомнить')

    # def __init__(self, request=None, *args, **kwargs):
    #     self.ip = kwargs.pop('ip', None)
    #     super().__init__(request, *args, **kwargs)
    #     self.fields['username'].label = 'Логин'
    #     self.fields['username'].label_suffix = ''
    #     self.fields['username'].widget.attrs.update({'class': 'input__input'})
    #     self.fields['password'].label_suffix = ''
    #     self.fields['password'].widget.attrs.update({'class': 'input__input'})
    #     self.fields['remember_me'].label_suffix = ''
    #     self.fields['remember_me'].widget.attrs.update({'class': 'hidden'})
    #
    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #
    #     # Ошибка если пользователь пытается слишком часто логиниться
    #     count = Settings.get_login_attempt_limit_count()
    #     period = Settings.get_login_block_period()
    #     login_cache = LoginAttemptCache(self.ip, username, count, period)
    #
    #     if login_cache.is_blocked():
    #         support_email = Settings.get_support_email()
    #         password_error_msg = f'Возможность авторизации временно заблокирована по причине превышения допустимого ' \
    #             f'количества попыток входа. Попробуйте позже или обратитесь в техническую поддержку: {support_email}".'
    #         raise forms.ValidationError(dict(password=password_error_msg), code='invalid')
    #     else:
    #         login_cache.add_count()
    #
    #     try:
    #         super().clean()
    #         if not self.errors:
    #             login_cache.delete_cache()
    #         return self.cleaned_data
    #     except forms.ValidationError as e:
    #         # Если пользователя не существует
    #         if username:
    #             try:
    #                 User.objects.get(username=username)
    #             except User.DoesNotExist:
    #                 raise forms.ValidationError(
    #                     {'username': 'Пользователь с таким логином не зарегистрирован'},
    #                     code=e.code,
    #                 )
    #         # подменяем ошибки, чтобы они были привязаны к полю
    #         if e.code == 'invalid_login':
    #             balance_count = login_cache.get_balance_count()
    #             raise forms.ValidationError(
    #                 {
    #                     'password': self.error_messages[
    #                                     'invalid_login'] + f', оставшееся количество попыток: {balance_count}'
    #                 },
    #                 code=e.code,
    #             )
    #         if e.code == 'inactive':
    #             raise forms.ValidationError(
    #                 {'username': self.error_messages['inactive'] + Settings.get_support_email()},
    #                 code=e.code,
    #             )
    #         else:
    #             raise e
