time = int(input('Введите количество секунд:'))
hours = time//3600
time = time % 3600
minutes = time // 60
time = time % 60
seconds = time
print("%02d:%02d:%02d" % (hours, minutes, seconds))
