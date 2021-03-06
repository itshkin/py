# Задача №1
"""1.Научите Анфису склонять слово "сообщения" в зависимости от их количества:
для 0 — 'У вас нет новых сообщений'
для 1 — 'У вас 1 новое сообщение'
от 2 до 4 — 'У вас # новых сообщения'
от 5 до 20 — 'У вас # новых сообщений'"""

# Решение
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')
    elif messages_count < 5:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        print('У вас ' + str(messages_count) + ' новых сообщений')

# Задача №2
"""Анфиса умеет здороваться утром и днём, но ей нужно добавить приветствия для ночи и вечера. Напишите условную 
конструкцию, которая выводит уместные сообщения: """

# Решение
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print('Доброй ночи!')  # напишите код здесь
    elif current_hour < 12:
        print('Доброе утро!')
    elif current_hour < 18:
        print('Добрый день!')
    elif current_hour < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')
