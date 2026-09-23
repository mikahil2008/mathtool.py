import sys
import math

from cli import build_parser
from calc import equation, stats, series, integration

def handle_solve(args):
    """Обработчик команды solve"""
    given = [args.a is not None, args.b is not None, args.c is not None]
    if any(given) and not all(given):
        raise ValueError("заданы не все коэффициенты")

    if all(given):
        a, b, c = args.a, args.b, args.c
    else:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        c = int(input("Введите C: "))

    equation.check_coefficients(a, b, c)
    kind, d, roots = equation.solve(a, b, c)

    print(f"Уравнение {kind}")
    if d is not None:
        print(f"Дискриминант: {d}")
    if len(roots) == 0:
        print("Действительных корней нет")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")

    return 0

def handle_stats(args):
    """Обработчик команды stats"""
    if args.input:
        with open(args.input, encoding="utf-8-sig") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    values = []
    for line in lines:
        for word in line.split():
            try:
                v = float(word)
            except ValueError:
                raise ValueError(f"{word} не является числом")
            values.append(v)

    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > stats.MAX_COUNT:
        raise ValueError("слишком много чисел")
    for v in values:
        if not math.isfinite(v):
            raise ValueError("значение не является конечным")
        if abs(v) > stats.MAX_ABS:
            raise ValueError("значение вне допустимого диапазона")

    for label, func, form in stats.REPORT:
        value = func(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")

    return 0

def handle_series(args):
    """Обработчик команды series"""
    term, formula = series.FORMULAS[args.func]

    if args.terms is not None:
        count = args.terms
        if not (1 <= count <= series.MAX_TERMS):
            raise ValueError("количество слагаемых вне диапазона")
        result, n = series.sum_by_count(term, count)
    else:
        eps = args.eps
        if not (math.isfinite(eps) and 0 < eps <= series.MAX_EPS):
            raise ValueError("точность вне диапазона")
        result, n = series.sum_by_eps(term, eps)

    print(formula)
    print(f"Слагаемых: {n}")
    print(f"Сумма ряда: {result:.{series.DIGITS}f}")

    return 0

def handle_integrate(args):
    """Обработчик команды integrate"""
    f, formula, low, high, inclusive = integration.FUNCTIONS[args.func]

    a = args.start
    b = args.to
    steps = args.steps

    if not (math.isfinite(a) and math.isfinite(b)):
        raise ValueError("предел не является конечным числом")
    if a >= b:
        raise ValueError("начальный предел не меньше конечного")
    if inclusive:
        if a < low or b > high:
            raise ValueError("предел вне промежутка")
    else:
        if a <= low or b >= high:
            raise ValueError("предел вне промежутка")
    if not (1 <= steps <= integration.MAX_STEPS):
        raise ValueError("количество шагов вне диапазона")

    print(formula)
    result = integration.integrate(f, a, b, steps)
    print(f"Значение интеграла: {result:.{integration.DIGITS}f}")

    return 0

HANDLERS = {
    "solve": handle_solve,
    "stats": handle_stats,
    "series": handle_series,
    "integrate": handle_integrate,
}

def main(argv):
    """Точка входа: разбор параметров и вызов обработчика"""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as e:
        print(f"ОШИБКА: {e}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
