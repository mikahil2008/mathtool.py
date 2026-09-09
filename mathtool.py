MAX_VALUE = 10000
import math
import sys
reference_data = """mathtool — решение уравнений вида A*x^2 + B*x + C = 0

Использование:
    python mathtool.py                         вывод справки
    python mathtool.py --help                  вывод справки
    python mathtool.py solve                   ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами

Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."""

if (len(sys.argv) == 1) or sys.argv[1] == '--help':
    print(reference_data)
    sys.exit(0)

if(len(sys.argv) == 2) and sys.argv[1] != 'solve':
    print('ОШИБКА: команда не найдена',file=sys.stderr)
    sys.exit(1)

if (len(sys.argv) == 2) and sys.argv[1] == 'solve':
    try:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        c = int(input('Введите третье число:'))
    except ValueError:
        print('ОШИБКА: коэффициенты не являются целыми числами',file=sys.stderr)
        sys.exit(1)
elif (len(sys.argv) == 8) and sys.argv[1] == 'solve':
    if (sys.argv[2] != '-a') or (sys.argv[4] != '-b') or (sys.argv[6] != '-c'):
        print('ОШИБКА: введен неизвестный параметр',file=sys.stderr)
        sys.exit(1)
    try:
        a = int(sys.argv[3])
        b = int(sys.argv[5])
        c = int(sys.argv[7])
    except ValueError:
        print('ОШИБКА: коэффициент не является целым числом',file=sys.stderr)
        sys.exit(1)
else:
    print('ОШИБКА: неверный набор параметров',file=sys.stderr)
    sys.exit(1)
if abs(a)>MAX_VALUE or abs(b)>MAX_VALUE or abs(c)>MAX_VALUE:
    print('ОШИБКА: значения коэффициентов по модулю превышают 10 000',file=sys.stderr)
    sys.exit(1)
elif a == 0 and b == 0:
    print('ОШИБКА: не уравнение - неизвестного нет',file=sys.stderr)
    sys.exit(1)
elif a == 0 and b != 0:
    print('Уравнение линейное')
    x = -c / b
    print(f'x = {x:.3f}')
    sys.exit(0)
else:
    D = b*b - 4 * a * c
    print('Квадратное уравнение','Дискриминант равен:',D)
    if D < 0:
        print('Корней нет')
        sys.exit(0)
    elif D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f'x1 = {x1:.3f}')
        print(f'x2 = {x2:.3f}')
        sys.exit(0)
    elif D == 0:
        x = -b / (2*a)
        print(f'x = {x:.3f}')
        sys.exit(0)