number = int(input('Введите число:'))
b = 0
while number > 0:
    a = number % 10
    number = number // 10
    if a > b:
        b = a
    if a <= b:
        continue
print(b)
