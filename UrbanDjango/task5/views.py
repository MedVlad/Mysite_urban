from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ["Kira", "Mira", "Yakob", "Dubel"]
info = {}


def check_user(users: list, name: str, pas: str, rep_pas: str, age: int) -> bool:
    if (name not in users) and (pas == rep_pas) and int(age) > 18:
        return True


def sign_up_by_html(request):
    global info
    if request.method == 'POST':
        username = request.POST.get('username').capitalize()
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if check_user(users, username, password, repeat_password, age):
            return HttpResponse(f'Приветствуем, {username}!')
        if username in users:
            info = {'error': 'Пользователь уже существует'}
        if int(age) < 18:
            info = {'error': 'Вы должны быть старше 18'}
        if password != repeat_password:
            info = {'error': 'Пароли не совпадают'}
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    global info
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].capitalize()
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if check_user(users, username, password, repeat_password, int(age)):
                return HttpResponse(f'Приветствуем, {username}!')
            if username.capitalize() in users:
                info = {'error': 'Пользователь уже существует'}
            elif int(age) < 18:
                info = {'error': 'Вы должны быть старше 18'}
            elif password != repeat_password:
                info = {'error': 'Пароли не совпадают'}
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)
