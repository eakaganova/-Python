# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input('Введи время в секундах: '))
secundes = user_time % 60
hours = user_time // 3600
minutes = (user_time % 3600) // 60
print(f'{hours:02d}:{minutes:02d}:{secundes:02d}')
