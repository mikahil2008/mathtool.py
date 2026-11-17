from calc.arrays import MIN_VALUE, MAX_VALUE

METHODS = {}

def _wrong_order(a, b, descending):
    """Истинно, если пара a, b стоит не в нужном порядке"""
    if descending:
        return a < b
    return a > b
def _earlier(a, b, descending):
    """Истино если a должно стоять раньше b"""
    return a < b

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
def _quick_range(values, left, right, descending):
    """Разбиение Хоара для диапазона left..right включительно"""
    while left < right:
        pivot = values[(left + right) // 2]
        i = left
        j = right
        while i <= j:
            while _earlier(values[i], pivot, descending):
                i += 1
            while _earlier(pivot, values[j], descending):
                j -= 1
            if i <= j:
                values[i], values[j] = values[j], values[i]
                i += 1
                j -= 1
        # рекурсивно обрабатываем меньшую часть, большую — в цикле,
        # чтобы глубина стека была O(log n)
        if j - left < right - i:
            _quick_range(values, left, j, descending)
            left = i
        else:
            _quick_range(values, i, right, descending)
            right = j

def quick(values, descending=False):
    """Быстрая сортировка Хоара"""
    _quick_range(values, 0, len(values) - 1, descending)

def _merge(values, left, middle, right, descending):
    """Сливает две упорядоченные части values[left..middle] и [middle+1..right]"""
    result = []
    i = left
    j = middle + 1
    while i <= middle and j <= right:
        if _earlier(values[j], values[i], descending):
            result.append(values[j])
            j += 1
        else:
            result.append(values[i])
            i += 1
    result.extend(values[i:middle + 1])
    result.extend(values[j:right + 1])
    values[left:right + 1] = result

def _merge_range(values, left, right, descending):
    """Рекурсивное разделение массива пополам"""
    if left >= right:
        return
    middle = (left + right) // 2
    _merge_range(values, left, middle, descending)
    _merge_range(values, middle + 1, right, descending)
    _merge(values, left, middle, right, descending)

def merge(values, descending=False):
    """Сортировка слиянием"""
    _merge_range(values, 0, len(values) - 1, descending)

def _sift(values, i, size, descending):
    """Просеивает элемент i вниз до нужного места в куче размера size"""
    while True:
        chosen = i
        for child in (2 * i + 1, 2 * i + 2):
            if child < size and _earlier(values[chosen], values[child], descending):
                chosen = child
        if chosen == i:
            return
        values[i], values[chosen] = values[chosen], values[i]
        i = chosen

def heap(values, descending=False):
    """Пирамидальная сортировка"""
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        _sift(values, i, n, descending)
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        _sift(values, 0, end, descending)

METHODS["bubble"] = bubble
METHODS["selection"] = selection
METHODS["insertion"] = insertion
METHODS["counting"] = counting
METHODS["quick"] = quick
METHODS["merge"] = merge
METHODS["heap"] = heap