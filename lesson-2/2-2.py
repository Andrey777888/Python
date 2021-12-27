a = list(map(int, input('Введите значения через пробел: ').split()))
f = list
s = len(a)
if s % 2 != 0:
    f = a[-1:]
    a.pop()
    a[::2], a[1::2] = a[1::2], a[::2]
    a.extend(f)
    print(a)
else:
    a[::2], a[1::2] = a[1::2], a[::2]
    print(a)
