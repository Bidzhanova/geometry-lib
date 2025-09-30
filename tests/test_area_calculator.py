import pytest
from math import pi
from geometry_lib import AreaCalculator, Circle, Triangle


class TestAreaCalculator:
    """Тесты для класса AreaCalculator."""

    def test_calculate_area_circle(self):
        """Тест вычисления площади круга через калькулятор."""
        circle = Circle(5)
        expected_area = pi * 25
        assert AreaCalculator.calculate_area(circle) == expected_area

    def test_calculate_area_triangle(self):
        """Тест вычисления площади треугольника через калькулятор."""
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        assert AreaCalculator.calculate_area(triangle) == pytest.approx(expected_area)

    def test_calculate_area_from_args_circle(self):
        """Тест вычисления площади круга по аргументам."""
        area = AreaCalculator.calculate_area_from_args(5)
        expected_area = pi * 25
        assert area == expected_area

    def test_calculate_area_from_args_triangle(self):
        """Тест вычисления площади треугольника по аргументам."""
        area = AreaCalculator.calculate_area_from_args(3, 4, 5)
        expected_area = 6.0
        assert area == pytest.approx(expected_area)

    def test_invalid_shape_creation(self):
        """Тест создания невалидной фигуры."""
        # Проверяем, что нельзя создать невалидные фигуры
        with pytest.raises(ValueError):
            Circle(-1)

        with pytest.raises(ValueError):
            Triangle(1, 1, 3)
