import argparse

from calc.series import FORMULAS
from calc.integration import FUNCTIONS

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

    return parser
