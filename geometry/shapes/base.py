from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный базовый класс для всех геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass

    def is_valid(self) -> bool:
        """
        Проверяет, является ли фигура валидной.
        По умолчанию возвращает True, если площадь > 0.
        """
        try:
            return self.area() > 0
        except (ValueError, TypeError):
            return False
