my_list = [7, 5, 3, 3, 2]
number = int(input('Введите новый элемент рейтинга: '))
my_list.append(number)
my_list.sort(reverse=True)
print(my_list)
