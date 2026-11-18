"""Поиск k-й порядковой статистики: разбиение Ломуто и quickselect"""
import random


def partition(values, left, right, rng):
    """Разбиение Ломуто: случайный опорный переносится в конец, элемент
    занимает окончательную позицию; возвращает её индекс"""
    q = rng.randint(left, right)
    values[q], values[right] = values[right], values[q]
    pivot = values[right]
    i = left
    for j in range(left, right):
        if values[j] <= pivot:
            values[i], values[j] = values[j], values[i]
            i += 1
    values[i], values[right] = values[right], values[i]
    return i


def statistic(values, k, seed=None):
    """Возвращает значение, которое стояло бы на месте k (с 1) после
    сортировки по возрастанию; меняет порядок списка, но не сортирует его"""
    if isinstance(k, bool) or not isinstance(k, int):
        raise ValueError("k должно быть целым числом")
    if not values:
        raise ValueError("массив пуст")
    if not 1 <= k <= len(values):
        raise ValueError("k вне диапазона 1..длина массива")

    rng = random.Random(seed)
    target = k - 1
    left = 0
    right = len(values) - 1
    while left < right:
        p = partition(values, left, right, rng)
        if target == p:
            return values[p]
        if target < p:
            right = p - 1
        else:
            left = p + 1
    return values[left]
