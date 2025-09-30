from typing import Union
from ..shapes.base import Shape


class AreaCalculator:
    """Калькулятор для вычисления площади фигур."""

    @staticmethod
    def calculate_area(shape: Shape) -> float:
        """Вычисляет площадь любой фигуры, наследующей от Shape."""
        return shape.area()

    @staticmethod
    def calculate_area_from_args(*args) -> float:
        """
        Вычисляет площадь фигуры без знания ее типа в compile-time.

        Args:
            *args: аргументы для создания фигуры (1 - круг, 3 - треугольник)

        Returns:
            Площадь фигуры
        """
        from ..shapes.shape_factory import ShapeFactory
        shape = ShapeFactory.create_shape(*args)
        return shape.area()
