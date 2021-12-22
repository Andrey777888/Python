profit = int(input('Введите значение прибыли:'))
costs = int(input('Введите значение издержек:'))
if profit > costs:
    prof = profit-costs
    rent = profit/prof
    print('Фирма работает в прибыль!')
    print('Рентабельность выручки: ', rent)
    staff = int(input('Введите количество сотрудников:'))
    profit_staff = prof/staff
    print(profit_staff, 'прибыль фирмы в расчёте на одного сотрудника')
else:
    print('Фирма работает в убыток!')
