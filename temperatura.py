import random
min_t = -30
max_t = 30
days = int(input('введите количество дней:'))
max_days = 0
temper = 0
temp = 0
for _ in range(days):
    temper = random.randint(min_t,max_t)
    print(temper,end='_')
    if temper > 0:
        temp += 1
    else: 
        temp = 0
    if max_days < temp:
        max_days = temp
print(f'\n\n дней макс {max_days} ')


