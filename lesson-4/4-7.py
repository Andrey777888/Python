def fact(num):
    f_num = 1
    for i in range(num+1):
        yield f'{i}!= {f_num}'
        f_num *= i+1
for el in fact(int(input('Введите число: '))):
    print(el)
