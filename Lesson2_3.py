# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Через list
number_month = int(input('Введи номер месяца в году: '))
name_month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                  'ноябрь', 'декабрь']
index_month = number_month - 1
if index_month == 0 or index_month == 1 or index_month == 11:
    season = 'зима'
elif index_month == 2 or index_month == 3 or index_month == 4:
    season = 'весна'
elif index_month == 5 or index_month == 6 or index_month == 7:
    season = 'лето'
else:
    season = 'осень'
print(f'Это {name_month[index_month]}! И это {season}!')

# Через dict
index_month = int(input('Введи номер месяца в году: '))
month_dict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль',
                8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}
if month_dict.get(index_month) == 'январь' or month_dict.get(index_month) == 'февраль' or \
        month_dict.get(index_month) == 'декабрь':
    season = 'зима'
elif month_dict.get(index_month) == 'март' or month_dict.get(index_month) == 'апрель' or \
        month_dict.get(index_month) == 'май':
    season = 'весна'
elif month_dict.get(index_month) == 'июнь' or month_dict.get(index_month) == 'июль' or \
        month_dict.get(index_month) == 'август':
    season = 'лето'
else:
    season = 'осень'
print(f'Это {month_dict.get(index_month)}! И это {season}!')