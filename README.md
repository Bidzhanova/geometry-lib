# Geometry Library

Библиотека для вычисления площадей геометрических фигур. Простая в использовании, расширяемая и надежная.

## 📦 Установка
```bash
# Клонируйте репозиторий или скачайте исходный код
git clone https://github.com/Bidzhanova/geometry-lib.git
cd geometry_lib

# Установите библиотеку
pip install .
```

## 🚀 Быстрый старт
```bash
from geometry_lib import Circle, Triangle, AreaCalculator

# Создание круга
circle = Circle(5)
print(f"Площадь круга: {circle.area():.2f}")  # 78.54

# Создание треугольника
triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area():.2f}")  # 6.00
print(f"Прямоугольный треугольник: {triangle.is_right_triangle()}")  # True
```
## 📚 Основное использование
1. Прямое создание фигур
```bash
from geometry_lib import Circle, Triangle

# Круг по радиусу
circle = Circle(10)
area = circle.area()  # ≈314.16

# Треугольник по трем сторонам
triangle = Triangle(6, 8, 10)
area = triangle.area()  # 24.0
is_right = triangle.is_right_triangle()  # True
```
2. Использование фабрики фигур
```bash
from geometry_lib import ShapeFactory

# Фабрика сама определяет тип фигуры по количеству аргументов
circle = ShapeFactory.create_shape(5)        # 1 аргумент = круг
triangle = ShapeFactory.create_shape(3, 4, 5) # 3 аргумента = треугольник

print(f"Площадь: {circle.area():.2f}")      # 78.54
print(f"Площадь: {triangle.area():.2f}")    # 6.00
```
3. Калькулятор площадей (полиморфизм)
```bash
from geometry_lib import AreaCalculator

# Вычисление площади без знания типа фигуры на этапе компиляции
area1 = AreaCalculator.calculate_area_from_args(7)           # круг
area2 = AreaCalculator.calculate_area_from_args(5, 12, 13)   # треугольник

print(f"Площадь круга: {area1:.2f}")     # ≈153.94
print(f"Площадь треугольника: {area2:.2f}")  # 30.00
```

## 🛠 API Reference
### Cycle
```bash
circle = Circle(radius: float)
```
* radius - положительное число

* **Методы:**

  * area() -> float - вычисляет площадь

  * is_valid() -> bool - проверяет валидность фигуры

### Triangle
```bash
triangle = Triangle(a: float, b: float, c: float)
```
* a, b, c - положительные числа, удовлетворяющие неравенству треугольника

* **Методы:**

  * area() -> float - вычисляет площадь по формуле Герона

  * is_right_triangle(tolerance=1e-9) -> bool - проверяет, прямоугольный ли треугольник

  * is_valid() -> bool - проверяет валидность фигуры

### ShapeFactory
```bash
# Создание фигур без явного указания типа
shape = ShapeFactory.create_shape(*args)
```
* *args:

  * 1 аргумент: создает круг

  * 3 аргумента: создает треугольник

### AreaCalculator
```bash
# Полиморфное вычисление площади
AreaCalculator.calculate_area(shape) -> float
AreaCalculator.calculate_area_from_args(*args) -> float
```

## ⚠️ Обработка ошибок
Библиотека выбрасывает понятные исключения:
```bash
from geometry_lib import Circle, Triangle

try:
    circle = Circle(-5)  # Отрицательный радиус
except ValueError as e:
    print(e)  # "Радиус должен быть положительным числом"

try:
    triangle = Triangle(1, 1, 3)  # Несуществующий треугольник
except ValueError as e:
    print(e)  # "Треугольник с такими сторонами не существует"
```

## 🧪 Тестирование
```bash
# Установите зависимости для тестирования
pip install pytest

# Запустите тесты
pytest tests/

# Запустите тесты с подробным выводом
pytest -v tests/
```

## 🔧 Расширение библиотеки
Чтобы добавить новую фигуру:

1. Создайте класс, наследующий от Shape

2. Реализуйте методы area() и is_valid()

3. Обновите ShapeFactory

Пример:
```bash
from geometry_lib.shapes.base import Shape

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2
    
    def is_valid(self) -> bool:
        return self.side > 0
```

## 📋 Требования

* Python 3.7+

* Для тестирования: pytest

## 🤝 Вклад в разработку

1. Форкните репозиторий

2. Создайте ветку для новой функциональности

3. Напишите тесты

4. Убедитесь, что все тесты проходят

5. Создайте Pull Request

## 📄 Лицензия

MIT License

## 💡 Примеры использования

### Вычисление площадей нескольких фигур

```bash
from geometry_lib import Circle, Triangle, AreaCalculator

figures = [
    Circle(3),
    Triangle(3, 4, 5),
    Triangle(5, 5, 5)
]

for figure in figures:
    area = AreaCalculator.calculate_area(figure)
    print(f"Площадь: {area:.2f}")
```

### Проверка валидности фигур

```bash
from geometry_lib import ShapeFactory

shapes_data = [
    (5,),           # валидный круг
    (3, 4, 5),      # валидный треугольник  
    (-2,),          # невалидный круг
    (1, 1, 3)       # невалидный треугольник
]

for args in shapes_data:
    try:
        shape = ShapeFactory.create_shape(*args)
        print(f"Фигура {args} валидна, площадь: {shape.area():.2f}")
    except ValueError as e:
        print(f"Фигура {args} невалидна: {e}")
```
