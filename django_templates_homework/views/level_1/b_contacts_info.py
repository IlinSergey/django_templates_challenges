from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

"""
Задания:
    1. Откройте страницу http://127.0.0.1:8000/contacts/ и наведите на вкладку в браузере, чтобы посмотреть ее название.
       Хотелось бы чего-то более осмысленного.
    2. Найдите в проекте темплэйт contacts_info.html, найдите там сообщение из первого пункта
       и исправьте на "Контактная информация".
    3. Откройте страницу http://127.0.0.1:8000/contacts/ и убедитесь,
       что теперь название вкладки соответствует содержанию.
"""


def contacts_info_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'level_1/contacts_info.html')
