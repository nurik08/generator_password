from cmath import e
from django.shortcuts import render
import random
import string

def index(request):
    characters = list(string.ascii_lowercase)
    try:
        lenght = int(request.GET.get('length'))
    except (TypeError, ValueError) as err:
        password = 'Вы не выбрали длину пароля'
        return render(request, 'gen_password/index.html', {'password':password})
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))
    the_password = ''
    for x in range(lenght):
        the_password += random.choice(characters)
    return render(request, 'gen_password/index.html', {'password':the_password})

