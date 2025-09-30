import pytest
from geometry_lib import Triangle


class TestTriangle:
    """Тесты для класса Triangle."""

    def test_area(self):
        """Тест вычисления площади треугольника."""
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        assert triangle.area() == pytest.approx(expected_area)

    def test_right_triangle(self):
        """Тест проверки прямоугольного треугольника."""
        right_triangle = Triangle(3, 4, 5)
        not_right_triangle = Triangle(3, 4, 6)

        assert right_triangle.is_right_triangle() is True
        assert not_right_triangle.is_right_triangle() is False

    def test_invalid_triangle_negative_sides(self):
        """Тест создания треугольника с отрицательными сторонами."""
        with pytest.raises(ValueError):
            Triangle(-1, 2, 3)

    def test_invalid_triangle_inequality(self):
        """Тест создания несуществующего треугольника."""
        with pytest.raises(ValueError):
            Triangle(1, 1, 3)

    def test_is_valid(self):
        """Тест проверки валидности треугольника."""
        valid_triangle = Triangle(3, 4, 5)
        assert valid_triangle.is_valid() is True

    def test_repr(self):
        """Тест строкового представления."""
        triangle = Triangle(3, 4, 5)
        assert repr(triangle) == "Triangle(sides=[3, 4, 5])"
