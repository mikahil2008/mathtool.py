import argparse

from calc.series import FORMULAS
from calc.integration import FUNCTIONS
from calc.sorting import METHODS


def build_parser():
    """Создание и настройка разборщика параметров"""
    parser = argparse.ArgumentParser(
        prog="mathtool",
        description="расчёты над уравнениями и числовыми последовательностями",
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")

    p_solve = subparsers.add_parser("solve", allow_abbrev=False,
                                    help="решение уравнения")
    p_solve.add_argument("-a", type=int, help="коэффициент A")
    p_solve.add_argument("-b", type=int, help="коэффициент B")
    p_solve.add_argument("-c", type=int, help="коэффициент C")

    p_stats = subparsers.add_parser("stats", allow_abbrev=False,
                                    help="показатели последовательности")
    p_stats.add_argument("--input", help="имя файла с числами")

    p_series = subparsers.add_parser("series", allow_abbrev=False,
                                     help="сумма ряда")
    p_series.add_argument("--func", required=True,
                          choices=sorted(FORMULAS),
                          help="какой ряд суммировать")
    group = p_series.add_mutually_exclusive_group(required=True)
    group.add_argument("--terms", type=int, help="количество слагаемых")
    group.add_argument("--eps", type=float, help="точность остановки")

    p_integrate = subparsers.add_parser("integrate", allow_abbrev=False,
                                        help="численное интегрирование")
    p_integrate.add_argument("--func", required=True,
                             choices=sorted(FUNCTIONS),
                             help="какую функцию интегрировать")
    p_integrate.add_argument("--from", dest="start", type=float, required=True,
                             help="нижний предел интегрирования")
    p_integrate.add_argument("--to", type=float, required=True,
                             help="верхний предел интегрирования")
    p_integrate.add_argument("--steps", type=int, required=True,
                             help="количество шагов")
    p_fill = subparsers.add_parser("fill", allow_abbrev=False,
                                   help="создание массива случайных чисел")
    p_fill.add_argument("-c", "--count", type=int, required=True,
                        help="количество элементов, от 1 до 1000000")
    p_fill.add_argument("--min", type=int, default=-100,
                        help="нижняя граница значений (по умолчанию -100)")
    p_fill.add_argument("--max", type=int, default=100,
                        help="верхняя граница значений (по умолчанию 100)")
    p_fill.add_argument("--seed", type=int, default=None,
                        help="начальное значение генератора")
    p_fill.add_argument("-o", "--output", default=None,
                        help="файл для созданного массива")

    p_sort = subparsers.add_parser("sort", allow_abbrev=False,
                                   help="сортировка массива")
    p_sort.add_argument("-m", "--method", required=True,
                        help=f"метод: {', '.join(sorted(METHODS))}")
    p_sort.add_argument("--order", choices=["asc", "desc"], default="asc",
                        help="направление сортировки (по умолчанию asc)")
    p_sort.add_argument("-i", "--input", default=None,
                        help="файл с исходным массивом")
    p_sort.add_argument("-o", "--output", default=None,
                        help="файл для отсортированного массива")

    p_search = subparsers.add_parser("search", allow_abbrev=False,
                                     help="двоичный поиск в массиве")
    p_search.add_argument("-v", "--value", type=int, required=True,
                          help="искомое целое число, модуль не больше 1000")
    p_search.add_argument("-i", "--input", default=None,
                          help="файл с массивом по возрастанию")

    return parser
