# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('Введи число от 1 до 99: '))
if user_number < 10:
    print(user_number*123)
else:
    print(user_number*10203)

# Решение преподавателя с урока
# n = input('Введи число: ')
# nn = n + n
# nnn = n + n + n
# result = int(n) + int(nn) + int(nnn)
# print(result)