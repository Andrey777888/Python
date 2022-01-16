def my_function(p_1, p_2):
    try:
        num = p_1 / p_2
        print(f'{p_1} / {p_2} = {num}')
    except ZeroDivisionError:
        print('Ошибка на 0 делить нельзя!')
my_function((int(input('Введите число №1:'))), int(input('Введите число №2:')))
