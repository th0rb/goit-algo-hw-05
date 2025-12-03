from timeit import timeit
from pathlib import Path

from bm_search import boyer_moore_search
from kmp_search import kmp_search
from rk_search import rabin_karp_search

base_path = Path(__file__).parent
article1_path = base_path / 'article_1.txt'
article2_path = base_path / 'article_2.txt'

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Завантаження статей
article1 = read_file(article1_path)
article2 = read_file(article2_path)

# Підрядки для тестування
patterns = ["Стаття", "Неіснуючий підрядок для тестування"]

# Функція для вимірювання часу виконання алгоритмів
def measure_time(algorithm, text, pattern):
    return timeit(lambda: algorithm(text, pattern), number=1000)

# Вимірювання часу для кожного алгоритму та підрядка
results = {}
for pattern in patterns:
    results[pattern] = {
        "Boyer-Moore": (
            measure_time(boyer_moore_search, article1, pattern),
            measure_time(boyer_moore_search, article2, pattern)
            ),
        "KMP": (
            measure_time(kmp_search, article1, pattern),
            measure_time(kmp_search, article2, pattern)
            ),
        "Rabin-Karp": (
            measure_time(rabin_karp_search, article1, pattern),
            measure_time(rabin_karp_search, article2, pattern)
            ),
    }

# Формування таблиці результатів
table_data = []
for pattern, result in results.items():
    for algo, times in result.items():
        table_data.append([pattern, algo, f"{times[0]:.6f}", f"{times[1]:.6f}"])

headers = ["Підрядок", "Алгоритм", "Стаття 1 (сек)", "Стаття 2 (сек)"]
table = (table_data, headers)

print(table)
