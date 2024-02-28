import math

per_day = int(input('Машина проезжает за день км: '))
total = int(input('Сколько нужно проехать км:  '))

print(math.ceil(total/per_day))
print(total//per_day + bool(total%per_day))
print(total//per_day + (total%per_day>0))
print((total + per_day - 1)//per_day)
print( -(-total//per_day))