from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f'Заработная плата-{time * rate + bonus}')
    except ValueError:
        print('Вводите только 3 числа')


salary()
