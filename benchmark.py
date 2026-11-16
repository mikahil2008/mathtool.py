import sys
from calc import arrays
from calc.sorting import bubble, insertion, selection, counting
from mathtool import measure

ALGORITHMS = (
    ("bubble", bubble),
    ("selection", selection),
    ("insertion", insertion),
    ("counting", counting),
)

def main(path):
    """Сравнивает время работы всех сортировок на одном массиве"""
    array = arrays.read_array(path)

    print(f"Элементов в массиве: {len(array)}")
    print(f"{'метод':<12}{'время, с':>14}")

    for name, sort in ALGORITHMS:
        # data.copy() — каждый алгоритм сортирует одинаковую копию исходного
        # массива, иначе первый же отсортирует его для всех остальных
        _, elapsed = measure(name, sort, [array.copy(), False], report=False)
        print(f"{name:<12}{elapsed:>14.6f}")

    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python benchmark.py <файл с массивом>",
              file=sys.stderr)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
