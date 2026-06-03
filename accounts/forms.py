import re

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME_PATTERN = re.compile(r'^[a-zA-Z0-9]{6,}$')


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        min_length=8,
        help_text='Не менее 8 символов.',
    )
    password_confirm = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        model = User
        fields = ('username', 'full_name', 'phone', 'email')
        labels = {
            'username': 'Логин',
            'full_name': 'ФИО',
            'phone': 'Контактный телефон',
            'email': 'E-mail',
        }
        help_texts = {
            'username': 'Латинские буквы и цифры, не менее 6 символов.',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
        self.fields['username'].widget.attrs.update({
            'pattern': '[a-zA-Z0-9]{6,}',
            'title': 'Латинские буквы и цифры, минимум 6 символов',
        })

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if not USERNAME_PATTERN.match(username):
            raise forms.ValidationError(
                'Логин должен содержать только латинские буквы и цифры '
                'и быть не короче 6 символов.'
            )
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким логином уже существует.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if len(password) < 8:
            raise forms.ValidationError('Пароль должен содержать не менее 8 символов.')
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Пароли не совпадают.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        max_length=150,
        widget=forms.TextInput(attrs={'autocomplete': 'username'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True

    def clean_username(self):
        return self.cleaned_data.get('username', '').strip()
