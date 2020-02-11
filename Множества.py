# Задача №1
"""
1.Сделайте из списка cities сет unique_cities, где записаны по разу названия городов, в которых живут ваши друзья.
После этого напечатайте строку из элементов unique_cities на экран через запятую — да, join() работает и для множеств
тоже!"""
# Решение
cities = ['Вологда', 'Чебоксары', 'Тольятти', 'Вологда']

unique_cities = set(cities)
separator = ', '
print(separator.join(unique_cities))

# Задача №2
"""2.Для каждого уникального города в списке cities напечатайте на экран сообщение Один мой друг живет в городе 
<название города>. """
# Решение
cities = ['Санкт-Петербург', 'Хабаровск', 'Казань', 'Санкт-Петербург', 'Казань']

# напишите ваш код здесь
unique_city = set(cities)
for city in unique_city:
    print('Один мой друг живет в городе', city)
