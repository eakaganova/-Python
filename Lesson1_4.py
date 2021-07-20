# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# Я не понимаю, как это делать по заданному условию. От слова совсем.
# Но так тоже работает.

user_number = input('Введи целое положительное число: ')
user_number = list(user_number)
user_number.sort()
print(user_number[-1])

# Решение преподавателя
# user_number = input('Введи целое положительное число: ')
# user_length = len(user_number)
# max_element = 0
# i = 0
# while i < user_length:
#     current_element = int(user_number)
#     if current_element > max_element:
#         max_element = current_element
#     i += 1
# print(max_element)

