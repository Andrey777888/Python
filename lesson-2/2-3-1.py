number = int(input('Введите месяц в виде целого числа от 1 до 12: '))
my_list = ['Зима', 'Весна', 'Лето', 'Осень']
if number == 12 or number == 1 or number == 2:
    print(my_list[0])
elif number == 3 or number == 4 or number == 5:
    print(my_list[1])
elif number == 6 or number == 7 or number == 8:
    print(my_list[2])
else:
    print(my_list[3])
