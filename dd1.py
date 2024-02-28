from random import randint

my_list = []
list_size = int(input('введите размер списка:'))
for _ in range(list_size):
    my_list.append(randint(0,10)) #добавляет в пустой список рандомные числа от 0 до 10
print(my_list)

number = int(input('введите число:'))
# print(my_list.count(number)) # каунт выводит числа повторяющиеся
count = 0
for item in my_list:
    for number == item:
        count += 1
print(count)