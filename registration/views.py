# registration/views.py

# registration/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        # Обработка данных формы регистрации
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Предположим, что у нас есть поле для выбора роли в форме

        # Проверяем, существует ли пользователь с таким именем
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует.')
            return redirect('register')  # Перенаправляем обратно на страницу регистрации

        # Создание пользователя
        user = User.objects.create_user(username=username, password=password)

        # Сохраняем роль пользователя в атрибут пользователя (можно использовать произвольные атрибуты пользователя)
        user.role = role
        user.save()

        # После успешной регистрации, перенаправляем пользователя на страницу приветствия
        return redirect('welcome', role=role)  # Используем имя URL-шаблона 'welcome'

    return render(request, 'registration/register.html')


def welcome(request, role):
    # Определяем текст приветствия в зависимости от роли пользователя
    if role == 'admin':
        message = 'Ура, ты админ!'
    elif role == 'worker':
        message = 'Ура, ты работник!'
    elif role == 'client':
        message = 'Ура, ты клиент!'
    else:
        message = 'Добро пожаловать!'

    # Отображаем страницу приветствия с сообщением о роли пользователя
    return render(request, 'registration/welcome.html', {'message': message})
