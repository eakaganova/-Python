# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_rating = [23, 18, 10, 5, 5, 4, 1]
user_number = int(input('Введи число: '))
if user_number in my_rating:
    position = my_rating.index(user_number)
    my_rating.insert(position, user_number)
    print(my_rating)
elif user_number > my_rating[0]:
    my_rating.insert(0, user_number)
    print(my_rating)
elif user_number < my_rating[-1]:
    my_rating.append(user_number)
    print(my_rating)
else:
    for rating in my_rating:
        if rating < user_number:
            new_index = my_rating.index(rating)
            my_rating.insert(new_index, user_number)
            print(my_rating)
            break
