import random
import sys

MIN_VALUE = -100
MAX_VALUE = 100
MAX_COUNT = 1_000_000
MAX_SEARCH = 1000

def generate(count, low=MIN_VALUE, high=MAX_VALUE, seed=None):
    """Создаёт список из count случайных чисел в диапазоне low..high"""
    random.seed(seed)
    values = []
    for _ in range(count):
        values.append(random.randint(low, high))
    return values

def check_values(values):
    """Проверяет количество элементов и диапазон значений"""
    if not 1 <= len(values) <= MAX_COUNT:
        raise ValueError("количество элементов вне диапазона 1..1000000")
    for value in values:
        if not MIN_VALUE <= value <= MAX_VALUE:
            raise ValueError(f"значение {value} вне диапазона -100..100")

def read_array(path=None):
    """Читает массив из файла или с клавиатуры.

    Разделители — пробельные символы и запятые. Ввод с клавиатуры
    завершается пустой строкой, строкой из пробелов или EOF.
    """
    if path is not None:
        with open(path, encoding="utf-8-sig") as f:
            text = f.read()
    else:
        lines = []
        print("Введите числа (пустая строка — конец ввода):", file=sys.stderr)
        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line.strip():
                break
            lines.append(line)
        text = " ".join(lines)

    text = text.replace(",", " ")
    try:
        values = [int(word) for word in text.split()]
    except ValueError:
        raise ValueError("во входных данных есть не целое число")
    check_values(values)
    return values

def write_array(path, values):
    """Печатает массив или записывает его в файл в UTF-8 одной строкой.

    Возвращает (количество элементов, имя файла или None).
    """
    line = " ".join(str(x) for x in values) + "\n"
    if path is not None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(line)
        return len(values), path
    print(line, end="")
    return len(values), None

def is_ordered(values):
    """Проверяет, что массив упорядочен по возрастанию (нестрого)"""
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            return False
    return True

def binary_search(values, target):
    """Двоичный поиск: индекс с нуля или None"""
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return None