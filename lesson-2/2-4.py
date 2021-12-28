my_list = list(map(str, input('Введите строку из нескольких слов, разделённых пробелом: ').split()))
my_list_2 = []
for i in range(len(my_list)):
    s = my_list[i][:10]
    my_list_2.append(s)
for i, v in enumerate(my_list_2, 1):
    print(f'{i}) {v}')
