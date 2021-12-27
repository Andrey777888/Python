a = float(input('Введите результат а:'))
b = float(input('Введите результат b:'))
i = 0
while a < b:
    i += 1
    a += a/10
    if a >= b:
        print(i+1)
