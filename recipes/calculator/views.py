from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'servings':{
        'яйца, шт': 8,
        'молоко, л': 0.4,
        'соль, ч.л.': 2.0,
    }
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calc_reciept(request, dish):
    msg = DATA[dish]
    quantity = request.GET.get('servings', 1)
    print(msg.keys())
    dictonary = {}
    for i in msg.keys():
        dictonary[i] = msg[i] * int(quantity)
    result = ';<br> '.join([f'{key}: {value}' for key, value in dictonary.items()])
    return HttpResponse(str(result))