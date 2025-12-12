"""probability_cheatsheet.py

Удобный модуль-«шпора» по двум разделам школьной математики:
1) Арифметические и геометрические прогрессии (формулы для n-го члена и суммы).
2) Базовые формулы теории вероятностей: условная вероятность, формула полной
   вероятности, независимость, вероятность объединения.

Файл содержит функции с типами, подробные docstring'и и небольшой раздел примеров.
"""

from typing import Optional


#########################
#  Последовательности  #
#########################


def arithmetic_n(u0: float, r: float, n: int) -> float:
	"""Возвращает n-й член арифметической прогрессии Un = U0 + n*r.

	Параметры:
	  u0 -- начальный член U0 (при n=0)
	  r  -- разность прогрессии
	  n  -- индекс (целое неотрицательное)
	"""
	return u0 + n * r


def arithmetic_sum(u0: float, r: float, n: int) -> float:
	"""Сумма первых n+1 членов S_n = U0 + U1 + ... + Un.

	Формула: S_n = (n+1) * (U0 + Un) / 2, где Un = U0 + n*r.
	"""
	un = arithmetic_n(u0, r, n)
	return (n + 1) * (u0 + un) / 2


def geometric_n(v0: float, q: float, n: int) -> float:
	"""Возвращает n-й член геометрической прогрессии Vn = V0 * q**n."""
	return v0 * (q ** n)


def geometric_sum(v0: float, q: float, n: int) -> float:
	"""Сумма первых n+1 членов геометрической прогрессии.

	Формула: S_n = V0 * (1 - q**(n+1)) / (1 - q)  (если q != 1).
	Если q == 1, то S_n = V0 * (n+1).
	"""
	if abs(q - 1.0) < 1e-12:
		return v0 * (n + 1)
	return v0 * (1 - q ** (n + 1)) / (1 - q)


#########################
#  Вероятности         #
#########################


def conditional_probability(p_a_and_b: float, p_a: float) -> Optional[float]:
	"""P(B | A) = P(A ∩ B) / P(A).

	Возвращает None если P(A) == 0.
	"""
	if p_a == 0:
		return None
	return p_a_and_b / p_a


def intersection_from_conditional(p_b_given_a: float, p_a: float) -> float:
	"""P(A ∩ B) = P(B | A) * P(A)."""
	return p_b_given_a * p_a


def total_probability_from_partition(p_a: float, p_b_given_a: float, p_b_given_not_a: float) -> float:
	"""Формула полной вероятности для разбивки на A и ¬A:

	P(B) = P(B|A)P(A) + P(B|¬A)P(¬A)
	"""
	p_not_a = 1 - p_a
	return p_b_given_a * p_a + p_b_given_not_a * p_not_a


def is_independent(p_a: float, p_b: float, p_a_and_b: float, tol: float = 1e-9) -> bool:
	"""Проверяет независимость A и B: P(A ∩ B) == P(A)*P(B) с допуском tol."""
	return abs(p_a_and_b - (p_a * p_b)) <= tol


def union_probability(p_a: float, p_b: float, p_a_and_b: float) -> float:
	"""P(A ∪ B) = P(A) + P(B) - P(A ∩ B)."""
	return p_a + p_b - p_a_and_b


#########################
#  Примеры / демонстрация#
#########################


def example_sequences() -> None:
	"""Показывает примеры расчётов для прогрессий."""
	print("=== Арифметическая прогрессия ===")
	u0, r = 1.0, 3.0
	for n in range(5):
		print(f"U_{n} = {arithmetic_n(u0, r, n):.6g}")
	print(f"Сумма первых 5 членов: S_4 = {arithmetic_sum(u0, r, 4):.6g}\n")

	print("=== Геометрическая прогрессия ===")
	v0, q = 2.0, 3.0
	for n in range(5):
		print(f"V_{n} = {geometric_n(v0, q, n):.6g}")
	print(f"Сумма первых 5 членов: S_4 = {geometric_sum(v0, q, 4):.6g}\n")


def example_probabilities() -> None:
	"""Демонстрация формул вероятностей на примере дерева (из материалов):

	P(A) = 0.2
	P(B | A) = 0.6
	P(B | ¬A) = 0.7
	"""
	print("=== Пример: дерево вероятностей ===")
	p_a = 0.2
	p_b_given_a = 0.6
	p_b_given_not_a = 0.7

	p_a_and_b = intersection_from_conditional(p_b_given_a, p_a)
	p_not_a = 1 - p_a
	p_not_a_and_b = intersection_from_conditional(p_b_given_not_a, p_not_a)
	p_b = total_probability_from_partition(p_a, p_b_given_a, p_b_given_not_a)

	print(f"P(A) = {p_a}")
	print(f"P(B|A) = {p_b_given_a}")
	print(f"P(B|¬A) = {p_b_given_not_a}\n")

	print(f"P(A ∩ B) = P(B|A)*P(A) = {p_a_and_b}")
	print(f"P(¬A ∩ B) = P(B|¬A)*P(¬A) = {p_not_a_and_b}")
	print(f"P(B) = P(A ∩ B) + P(¬A ∩ B) = {p_b}\n")

	# Проверка независимости
	independent = is_independent(p_a, p_b, p_a_and_b)
	if independent:
		print("A и B независимы (P(A ∩ B) = P(A)*P(B)).")
	else:
		print("A и B НЕ независимы.")
		print(f"P(A)*P(B) = {p_a * p_b} != P(A ∩ B) = {p_a_and_b}")


def _pretty_header(title: str) -> None:
	print('\n' + '=' * 60)
	print(title)
	print('=' * 60 + '\n')


def main() -> None:
	_pretty_header('Шпора: прогрессии')
	example_sequences()
	_pretty_header('Шпора: вероятности')
	example_probabilities()


if __name__ == '__main__':
	main()

