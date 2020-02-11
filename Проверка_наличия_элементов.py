# Задача №1
"""Вы собираетесь поехать в Хабаровск. Было бы здорово встретиться там с друзьями. Но живет ли сейчас хоть кто-то из
друзей в Хабаровске? Научите Анфису отвечать на этот вопрос — сделайте ей функцию is_anyone_in(collection, city) """


# Первый  вариант решения
def is_anyone_in(collection, city):
    if city == collection:  # если есть среди значений словаря collection
        for name in friends:  # переберите все ключи словаря
            if friends == city:  # если соответствующее ключу значение равно city
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')


friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')


# Второй вариант решения
def is_anyone_in(collection, city):
    if city in collection.values():
        for name in collection.keys():
            if collection[name] == city:
                print('В городе ' + city + ' живёт ' + name + '.')
    else:
        print('Пока никого.')

friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}

is_anyone_in(friends, 'Хабаровск')