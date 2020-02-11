# Задача №1
"""1. Если вы захотите научить Анфису играть в города, ей нужно будет уметь выбирать город из множества городов,
которые она знает, исключая те, что уже были названы. Напишите функцию print_valid_cities, которая сравнит множество
всех городов all_cities со множеством названных городов used_cities и: создаст множество городов, которые ещё можно
использовать, напечатает такое множество на экран, разделяя города запятой. Запустите эту функцию на примерах разных
множеств и посмотрите, как она работает. """


# напишите код функции print_valid_cities, которая
# принимает аргументы all_cities и used_cities
def print_valid_cities(allCities, useCities):
    notUsedCities = allCities.difference(useCities)
    print(','.join(notUsedCities))


all_cities = {'Абакан', 'Астрахань', 'Бобруйск', 'Калуга', 'Караганда', 'Кострома', 'Липецк', 'Новосибирск'}

used_cities = {'Калуга', 'Абакан', 'Новосибирск'}
print_valid_cities(all_cities, used_cities)

# Задача №2
"""2. Научите Анфису помогать вам с покупками в магазине. Вы хотите приготовить два блюда и рассказываете Анфисе, 
какие для них нужны продукты. Напишите функцию print_shopping_list(), которая будет получать два списка продуктов 
—recipe1 и recipe2, и печатать на экран полный список покупок. Элементы в списке не должны повторяться. """


def print_shopping_list(recipe1, recipe2):
    pizza_set, salad_set = set(pizza), set(salad)
    shopping_list = pizza_set.union(salad_set)
    print(','.join(shopping_list))
    # напишите здесь свою функцию


pizza = ['мука', 'помидоры', 'шампиньоны', 'сыр', 'оливковое масло']
salad = ['огурцы', 'перцы', 'помидоры', 'оливковое масло', 'листья салата']

print_shopping_list(pizza, salad)

# Задача №3
"""3. Если вам надо 5 кг помидоров для салата и 3 кг для супа, вы сразу покупаете 8 килограммов. Напишите функцию, 
которая напечатает на экран, какие продукты надо купить, и сколько их нужно. Информацию о каждом ингредиенте выводите 
на отдельной строке в формате: огурцы, кг: 1.5. Каждый продукт должен присутствовать в выводе только один раз. """


def print_shopping_list(pizza,salad):
    dish = set(pizza)
    dish = dish.union(salad)

    for i in dish:
        weight = 0
        if i in pizza.keys(): weight += pizza[i]
        if i in salad.keys(): weight += salad[i]
        print(i, ': ', weight, sep='')


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}
salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
