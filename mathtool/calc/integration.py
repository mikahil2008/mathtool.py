import math

MAX_STEPS = 100000
DIGITS = 4

def f_ratio(x):
    """F(x) = x / (x + 1)"""
    return x / (x + 1)

def f_root(x):
    """F(x) = sqrt(x² + 1)"""
    return math.sqrt(x * x + 1)

FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0, 20, True),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5, 5, False),
}

def integrate(f, a, b, steps):
    """Численное интегрирование методом левых прямоугольников"""
    dx = (b - a) / steps
    result = 0
    for i in range(steps):
        x = a + i * dx
        result += f(x) * dx
    return result
