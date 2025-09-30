import pytest
from geometry import ShapeFactory, Circle, Triangle


class TestShapeFactory:
    """Тесты для класса ShapeFactory."""

    def test_create_circle(self):
        """Тест создания круга через фабрику."""
        shape = ShapeFactory.create_shape(5)
        assert isinstance(shape, Circle)
        assert shape.radius == 5

    def test_create_triangle(self):
        """Тест создания треугольника через фабрику."""
        shape = ShapeFactory.create_shape(3, 4, 5)
        assert isinstance(shape, Triangle)
        assert shape.sides == [3, 4, 5]

    def test_invalid_arguments(self):
        """Тест создания фигуры с неправильным количеством аргументов."""
        with pytest.raises(ValueError):
            ShapeFactory.create_shape(1, 2)  # 2 аргумента не поддерживаются

    def test_factory_with_invalid_circle(self):
        """Тест создания невалидного круга через фабрику."""
        with pytest.raises(ValueError):
            ShapeFactory.create_shape(-1)

    def test_factory_with_invalid_triangle(self):
        """Тест создания невалидного треугольника через фабрику."""
        with pytest.raises(ValueError):
            ShapeFactory.create_shape(1, 1, 3)
