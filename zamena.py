inp = [1,2,3,4,5]
k = 2
list1 = []
for i in range(len(inp)): # переводит список в множество
    list1.append(inp[i-k]) # добавляем в новый список i это номер индекса
print(list1)

# срез
my_list = [1,2,3,4,5]
shift = int(input('Введите сдвиг:')) # например 3
my_list = my_list[-shift:] + my_list[:-shift] # берем из списка -3: т.е.три последн числа и до конца плюсуем первые числа до -3
print(my_list)

# цикл
my_list = [1,2,3,4,5]
shift = int(input('Введите сдвиг:'))
for _ in range(shift): # сколько нам нужно сдвигать
    my_list.insert(0, my_list.pop(-1)) # инсерт-указывает куда добавлять элемент.(0-индекс)поп-удаляет элемент(указываем также индекс -1)
print(my_list)