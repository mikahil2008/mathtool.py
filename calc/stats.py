import math

MAX_ABS = 10000
MAX_COUNT = 20

def count(values):
    """Количество чисел."""
    return len(values)

def total(values):
    """Сумма чисел."""
    result = 0
    for v in values:
        result += v
    return result

def mean(values):
    """Среднее арифметическое."""
    return total(values) / len(values)

def sum_squares(values):
    """Сумма квадратов."""
    result = 0
    for v in values:
        result += v ** 2
    return result

def rms(values):
    """Среднее квадратическое."""
    return math.sqrt(sum_squares(values) / len(values))

def sum_sq_dev(values):
    """Сумма квадратов отклонений от среднего."""
    m = mean(values)
    result = 0
    for v in values:
        result += (v - m) ** 2
    return result

def variance(values):
    """Дисперсия (по N)."""
    return sum_sq_dev(values) / len(values)

def std_dev(values):
    """СКО — корень из дисперсии."""
    return math.sqrt(variance(values))

def standard_deviation(values):
    """Стандартное отклонение (по N-1)."""
    if len(values) < 2:
        return None
    return math.sqrt(sum_sq_dev(values) / (len(values) - 1))

def minimum(values):
    """Наименьшее значение."""
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result

def maximum(values):
    """Наибольшее значение."""
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result

def count_positive(values):
    """Количество положительных чисел."""
    result = 0
    for v in values:
        if v > 0:
            result += 1
    return result

def count_negative(values):
    """Количество отрицательных чисел."""
    result = 0
    for v in values:
        if v < 0:
            result += 1
    return result

REPORT = [
    ("Количество", count, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", sum_squares, ".3f"),
    ("Ср. кв.", rms, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", std_dev, ".3f"),
    ("Станд. откл.", standard_deviation, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", count_positive, "d"),
    ("Отрицательных", count_negative, "d"),
]
