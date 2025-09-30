from .base import Shape
from math import pi


class Circle(Shape):
    """Класс для представления круга."""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга: π * r²"""
        return pi * self.radius ** 2

    def is_valid(self) -> bool:
        """Круг всегда валиден после создания."""
        return True

    def __repr__(self):
        return f"Circle(radius={self.radius})"
