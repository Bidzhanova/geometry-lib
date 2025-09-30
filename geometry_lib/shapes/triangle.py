from .base import Shape
from math import isclose


class Triangle(Shape):
    """Класс для представления треугольника."""

    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.sides = [side_a, side_b, side_c]

        # Проверка на положительные стороны
        if any(side <= 0 for side in self.sides):
            raise ValueError("Все стороны треугольника должны быть положительными")

        # Проверка неравенства треугольника
        if not self._is_triangle_inequality_satisfied():
            raise ValueError("Треугольник с такими сторонами не существует")

    def area(self) -> float:
        """Вычисляет площадь по формуле Герона."""
        a, b, c = self.sides
        s = (a + b + c) / 2  # полупериметр
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def is_valid(self) -> bool:
        """Треугольник всегда валиден после создания."""
        return True

    def is_right_triangle(self, tolerance: float = 1e-9) -> bool:
        """Проверяет, является ли треугольник прямоугольным."""
        a, b, c = sorted(self.sides)
        return isclose(a ** 2 + b ** 2, c ** 2, rel_tol=tolerance)

    def _is_triangle_inequality_satisfied(self) -> bool:
        """Проверяет неравенство треугольника."""
        a, b, c = self.sides
        return (a + b > c) and (a + c > b) and (b + c > a)

    def __repr__(self):
        return f"Triangle(sides={self.sides})"
