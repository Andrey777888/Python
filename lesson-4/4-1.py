from sys import argv
def script_zp():
    try:
        hours, rate, bonus = map(float, argv[1:])
        print(f'zp: {hours*rate+bonus}')
    except ValueError:
        print('ERROR')
script_zp()
