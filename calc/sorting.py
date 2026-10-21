from calc.arrays import MIN_VALUE, MAX_VALUE

METHODS = {}

def _wrong_order(a, b, descending):
    """Истинно, если пара a, b стоит не в нужном порядке"""
    if descending:
        return a < b
    return a > b

def bubble(values, descending=False):
    """Сортировка пузырьком"""
    n = len(values)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if _wrong_order(values[j], values[j + 1], descending):
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break

def selection(values, descending=False):
    """Сортировка выбором"""
    n = len(values)
    for i in range(n - 1):
        best = i
        for j in range(i + 1, n):
            if _wrong_order(values[best], values[j], descending):
                best = j
        values[i], values[best] = values[best], values[i]

def insertion(values, descending=False):
    """Сортировка вставками"""
    n = len(values)
    for i in range(1, n):
        current = values[i]
        j = i
        while j > 0 and _wrong_order(values[j - 1], current, descending):
            values[j] = values[j - 1]
            j -= 1
        values[j] = current


def counting(values, descending=False):
    """Сортировка подсчётом"""
    size = MAX_VALUE - MIN_VALUE + 1
    counters = [0] * size
    for value in values:
        counters[value - MIN_VALUE] += 1

    k = 0
    indices = range(size)
    if descending:
        indices = reversed(indices)
    for number in indices:
        for _ in range(counters[number]):
            values[k] = number + MIN_VALUE
            k += 1

METHODS["bubble"] = bubble
METHODS["selection"] = selection
METHODS["insertion"] = insertion
METHODS["counting"] = counting