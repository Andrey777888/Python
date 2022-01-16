def my_info(p_1, p_2, p_3, p_4, p_5, p_6):
    print('my_info')
    return f'Фамилия:{p_2}, Имя:{p_1}, Год рождения:{p_3}, Город проживания:{p_4}, Email:{p_5}, Телефон:{p_6}'
print(my_info((str(input('имя: '))), str(input('фамилия: ')), (str(input('год рождения: '))),
              str(input('город проживания: ')), (str(input('email: '))), str(input('телефон:'))))
