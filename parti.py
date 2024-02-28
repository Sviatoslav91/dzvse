
vagon = int(input('Вы сели в вагон по счет от головы поезда?: '))
nomer = int(input('Введите ваш номер вагона: ')) 
if vagon == nomer:
    result = 'Без дополнительной информации задачу не решить '
else:
    result = ((vagon - 1) + nomer)
print( result)