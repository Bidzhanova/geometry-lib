from typing import Union
from .circle import Circle
from .triangle import Triangle


class ShapeFactory:
    """Фабрика для создания фигур без знания их типа в compile-time."""

    @staticmethod
    def create_shape(*args) -> Union[Circle, Triangle]:
        """
        Создает фигуру на основе переданных аргументов.

        Args:
            *args:
                - 1 аргумент: создает круг (радиус)
                - 3 аргумента: создает треугольник (3 стороны)

        Returns:
            Созданная фигура (Circle или Triangle)

        Raises:
            ValueError: если количество аргументов не поддерживается
        """
        if len(args) == 1:
            return Circle(args[0])
        elif len(args) == 3:
            return Triangle(*args)
        else:
            raise ValueError(
                f"Неподдерживаемое количество аргументов: {len(args)}. "
                "Поддерживается: 1 (круг) или 3 (треугольник)"
            )

    @staticmethod
    def create_valid_shape(*args) -> Union[Circle, Triangle]:
        """
        Создает фигуру и проверяет её валидность.

        Returns:
            Валидная фигура

        Raises:
            ValueError: если фигура невалидна
        """
        shape = ShapeFactory.create_shape(*args)

        # Проверяем валидность через вычисление площади
        try:
            shape.area()
            return shape
        except ValueError as e:
            raise ValueError(f"Созданная фигура невалидна: {e}")
