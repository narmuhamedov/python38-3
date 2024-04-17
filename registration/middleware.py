# registration/middleware.py

from django.contrib import messages
from django.shortcuts import redirect

class RegistrationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, если пользователь отправил форму регистрации
        if request.method == 'POST' and request.path == '/register/':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Простейшая проверка: убеждаемся, что пароль имеет не менее 6 символов
            if len(password) < 6:
                messages.error(request, 'Пароль должен содержать не менее 6 символов.')
                return redirect('register')

        return self.get_response(request)
