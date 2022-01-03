def my_func(p_1, p_2, p_3):
    min_num = min(p_1, p_2, p_3)
    sum = (p_1 + p_2 + p_3) - min_num
    return sum
print(my_func(int(input('Первое число: ')), int(input('Второе число: ')), int(input('Третье число: '))))
