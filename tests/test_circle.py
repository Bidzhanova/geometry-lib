import pytest
from math import pi
from geometry_lib import Circle


class TestCircle:
    """Тесты для класса Circle."""

    def test_area(self):
        """Тест вычисления площади круга."""
        circle = Circle(5)
        expected_area = pi * 25
        assert circle.area() == expected_area

    def test_negative_radius(self):
        """Тест создания круга с отрицательным радиусом."""
        with pytest.raises(ValueError):
            Circle(-1)

    def test_zero_radius(self):
        """Тест создания круга с нулевым радиусом."""
        with pytest.raises(ValueError):
            Circle(0)

    def test_is_valid(self):
        """Тест проверки валидности круга."""
        valid_circle = Circle(5)
        assert valid_circle.is_valid() is True

    def test_repr(self):
        """Тест строкового представления."""
        circle = Circle(3)
        assert repr(circle) == "Circle(radius=3)"
