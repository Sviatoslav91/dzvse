from random import randint

my_list = []
list_size = int(input('введите размер списка:'))
for _ in range(list_size):
    my_list.append(randint(0,100)) #добавляет в пустой список рандомные числа от 0 до 10
print(my_list)

number = int(input('введите число:'))
if my_list.count(number) > 0:
    result = f'Число {number} встречается в списке {my_list.count(number)} раз'
else:
    min_dictance = abs(my_list[0] - number) # берем модуль чисел то есть минус как плюс
    nearest_item = my_list[0]
    for i in range(1, len(my_list)): 
        if abs(my_list[i] - number) < min_dictance:
            min_dictance = abs(my_list[i] - number)
            nearest_item = my_list[i]
    result = f'Близжайшее число к {number} это {nearest_item}'        
print(result)