import random
min = 1
max = 70000

for_me = min
for_her = max

count = int(input('Введите количество арбузов:'))
for _ in range(count):
    arbuz = random.randint(min,max)
    print(arbuz,end='-')
    if arbuz < for_her:
        for_her=arbuz
    if arbuz > for_me:
        for_me = arbuz
print(f'\n\nарбуз для меня - {for_me} гр. \nарбуз для тещи - {for_her} гр.')


