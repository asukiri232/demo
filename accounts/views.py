from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, RegistrationForm

User = get_user_model()


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('cabinet')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if not User.objects.filter(username=username).exists():
                form.add_error(
                    None,
                    f'Пользователь с логином «{username}» не найден. '
                    'Проверьте правильность логина или пройдите регистрацию.',
                )
            else:
                user = authenticate(request, username=username, password=password)
                if user is None:
                    form.add_error(
                        None,
                        'Неверный пароль. Проверьте ввод и попробуйте снова.',
                    )
                elif not user.is_active:
                    form.add_error(
                        None,
                        'Учётная запись отключена. Обратитесь к администратору.',
                    )
                else:
                    login(request, user)
                    return redirect('cabinet')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def cabinet(request):
    user = request.user
    return render(request, 'accounts/cabinet.html', {
        'profile': {
            'full_name': user.full_name,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'date_joined': user.date_joined,
            'last_login': user.last_login,
        },
    })


@login_required
@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    return redirect('login')


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.user.is_authenticated:
        return redirect('cabinet')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def register_success(request):
    return render(request, 'accounts/register_success.html')
