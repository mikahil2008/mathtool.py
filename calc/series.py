import math

MAX_TERMS = 10000
MAX_EPS = 0.0001
MAX_ITERATIONS = 100000
DIGITS = math.ceil(-math.log10(MAX_EPS))

def sign(n):
    if n % 2 == 0:
        return -1
    return 1

def term_sqplus(n):
    return sign(n) / (n * n + 1)

def term_third(n):
    return sign(n) / (3 * n)

FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - ..."),
}

def sum_by_count(term, count):
    """Сумма первых count слагаемых"""
    result = 0
    for n in range(1, count + 1):
        result += term(n)
    return result, count


def sum_by_eps(term, eps):
    """Сумма слагаемых до достижения точности eps"""
    result = 0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")

