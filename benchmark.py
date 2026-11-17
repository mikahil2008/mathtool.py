"""Сравнение времени всех семи методов сортировки (таблица для отчёта)"""
import subprocess
import sys
import re

SIZES = (1000, 3000, 10000)
RUNS = 3
METHODS = ("bubble", "selection", "insertion",
           "counting", "quick", "merge", "heap")


def extract_time(stderr_text):
    """Достаёт время из строки stderr (первое число вида 0.123456)"""
    match = re.search(r"([0-9]+\.[0-9]+)", stderr_text)
    if match is None:
        raise RuntimeError(f"не найдено время: {stderr_text}")
    return float(match.group(1))


def main():
    """Готовит файлы данных, запускает sort и печатает таблицу"""
    print(f"{'Количество':<12}{'Метод':<12}"
          f"{'t1':>12}{'t2':>12}{'t3':>12}{'Среднее':>12}")

    for size in SIZES:
        data_file = f"data_{size}.txt"
        subprocess.run([sys.executable, "mathtool.py", "fill",
                        "-c", str(size), "--seed", "1", "-o", data_file],
                       check=True)

        for method in METHODS:
            times = []
            first_output = None
            same = True
            for run in range(RUNS):
                output = f"result_{method}.txt"
                proc = subprocess.run(
                    [sys.executable, "mathtool.py", "sort",
                     "-m", method, "-i", data_file, "-o", output],
                    capture_output=True, text=True, check=True)
                times.append(extract_time(proc.stderr))

                # сверяем, что все методы дают одинаковый результат
                with open(output, encoding="utf-8") as f:
                    current = f.read()
                if first_output is None:
                    first_output = current
                elif current != first_output:
                    same = False

            flag = "" if same else "  (! результаты различаются)"
            average = sum(times) / RUNS
            print(f"{size:<12}{method:<12}"
                  f"{times[0]:>12.6f}{times[1]:>12.6f}{times[2]:>12.6f}"
                  f"{average:>12.6f}{flag}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

