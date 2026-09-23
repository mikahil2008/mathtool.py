import math

MAX_VALUE = 10000


def check_coefficients(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        raise ValueError("коэффициент вне допустимого диапазона")
    if a == 0 and b == 0:
        raise ValueError("не уравнение - неизвестного нет")


def solve(a, b, c):
    if a == 0:
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c
    if d < 0:
        return "квадратное", d, []
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return "квадратное", d, [x1, x2]
    return "квадратное", d, [-b / (2 * a)]
