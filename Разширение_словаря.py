# Задача №1
"""Добавьте в словарь friends ещё две пары ключ-значение, просто дописав их в объявление словаря. Имена друзей и
города, в которых они живут, придумайте сами. После этого напечатайте на экран сообщение "Вот в каких городах живут
мои друзья: " и затем названия всех городов словаря, разделённые запятой с пробелом. """
#Решение
friends = {'Серёга': 'Омск', 'Соня': 'Москва', 'Дима': 'Челябинск', 'Филипп': 'Италия', 'Юлия': 'Париж'}
print("Вот в каких городах живут мои друзья: ", ','.join(friends.values()))
