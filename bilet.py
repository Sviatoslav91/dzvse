n = int(input('Введите шестизначное число: '))
a = n//100000 
b = (n%100000)//10000
c = (n%10000)//1000
q=a+b+c
e = n%10
r = (n%100)//10
t = (n%1000)//100
y=e+r+t
if q == y:
    print('yes')
else:
    print('no')