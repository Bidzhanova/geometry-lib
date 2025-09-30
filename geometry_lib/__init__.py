"""
Geometry Library - библиотека для вычисления площадей геометрических фигур.

Доступные классы:
- Circle: круг по радиусу
- Triangle: треугольник по трем сторонам
- ShapeFactory: фабрика для создания фигур
- AreaCalculator: калькулятор площадей
"""

from .shapes.circle import Circle
from .shapes.triangle import Triangle
from .shapes.shape_factory import ShapeFactory
from .calculators.area_calculator import AreaCalculator

__version__ = "1.0.0"
__all__ = ['Circle', 'Triangle', 'ShapeFactory', 'AreaCalculator']
