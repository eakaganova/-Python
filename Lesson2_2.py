# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list2 = list(input('Введите произвольный текст. Он может включать в себя любые символы, которые '
                 'Вы найдете на своей клавиатуре. Ни в чем себе не отказывайте :) '))
print(my_list2)
even_number = 0
odd_number = 1
while odd_number < len(my_list2):
    my_list2[even_number], my_list2[odd_number] = my_list2[odd_number], my_list2[even_number]
    even_number = even_number + 2
    odd_number = odd_number + 2
print(my_list2)

