# Ход решения
# 1. Создание структуры данных (Circle):
# Согласно условию, круг определяется радиусом и точкой центра. 
# Центр является вложенным объектом Point.
# 2. Функция point_in_circle:Точка находится внутри круга (или на границе), 
# если расстояние от неё до центра круга меньше или равно радиусу.
# Формула расстояния: d = ((x1-x2)**2 + (y1-y2)**2)**1/2, (или sqrt())
# Чтобы избежать медленного вычисления квадратного корня, мы можем сравнивать квадраты: d**2 <= radius**2
# 3. Функция rect_in_circle:
# Прямоугольник полностью находится внутри круга, если все 4 его угла находятся внутри этого круга
# Зная левый нижний угол (x, y), ширину w и высоту h (p. 4), мы находим остальные три угла: (x + w, y), (x, y + h) и (x + w, y + h)
# Затем для каждого угла вызываем созданную ранее point_in_circle
# Функция rect_circle_overlap:
# По условию достаточно проверить, находится ли хотя бы один из четырех углов прямоугольника внутри круга. Если да — возвращаем True
import math
import copy

class Point:
    """Представление точки в двумерном пространстве."""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Rectangle:
    """Определяет прямоугольник с атрибутами width, height и corner (Point)."""
    def __init__(self, width=0.0, height=0.0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner if corner is not None else Point()

class Circle:
    """Определяет круг с атрибутами center (Point) и radius."""
    def __init__(self, center=None, radius=0.0):
        self.center = center if center is not None else Point()
        self.radius = radius

def point_in_circle(circle: Circle, point: Point) -> bool:
    """Возвращает True, если точка лежит внутри круга или на его границе.
    
    >>> c = Circle(Point(150, 100), 75)
    >>> point_in_circle(c, Point(150, 100)) # Точно в центре
    True
    >>> point_in_circle(c, Point(150, 175)) # На верхней границе
    True
    >>> point_in_circle(c, Point(230, 100)) # За пределами радиуса (расстояние 80 > 75)
    False
    """
    # Вычисляем квадрат расстояния между точкой и центром круга
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance_sq = dx**2 + dy**2
    
    # Сравниваем с квадратом радиуса
    return distance_sq <= circle.radius**2

def get_rect_vertices(rect: Rectangle):
    """Вспомогательная функция для получения координат всех 4 углов прямоугольника."""
    p1 = rect.corner  # Левый нижний
    p2 = Point(p1.x + rect.width, p1.y)  # Правый нижний
    p3 = Point(p1.x, p1.y + rect.height)  # Левый верхний
    p4 = Point(p1.x + rect.width, p1.y + rect.height)  # Правый верхний
    return [p1, p2, p3, p4]

def rect_in_circle(circle: Circle, rect: Rectangle) -> bool:
    """Возвращает True, если прямоугольник полностью лежит внутри круга.
    
    >>> c = Circle(Point(150, 100), 75)
    >>> r1 = Rectangle(30, 40, Point(140, 80)) # Полностью внутри
    >>> rect_in_circle(c, r1)
    True
    >>> r2 = Rectangle(100, 100, Point(100, 50)) # Выглядывает углами наружу
    >>> rect_in_circle(c, r2)
    False
    """
    # Прямоугольник внутри, если ВСЕ его вершины внутри круга
    for vertex in get_rect_vertices(rect):
        if not point_in_circle(circle, vertex):
            return False
    return True

def rect_circle_overlap(circle: Circle, rect: Rectangle) -> bool:
    """Возвращает True, если хотя бы один угол прямоугольника находится внутри круга.
    
    >>> c = Circle(Point(150, 100), 75)
    >>> r1 = Rectangle(50, 50, Point(200, 100)) # Правый нижний угол за кругом, левые внутри
    >>> rect_circle_overlap(c, r1)
    True
    >>> r2 = Rectangle(10, 10, Point(0, 0)) # Далеко в стороне
    >>> rect_circle_overlap(c, r2)
    False
    """
    # Пересечение есть, если ХОТЯ БЫ ОДНА вершина попала в круг
    for vertex in get_rect_vertices(rect):
        if point_in_circle(circle, vertex):
            return True
    return False

if __name__ == '__main__':
    # Выполняем условие: создать объект Circle (центр 150, 100, радиус 75)
    my_circle = Circle(Point(150, 100), 75)
    print(f"Создан круг с центром ({my_circle.center.x}, {my_circle.center.y}) и радиусом {my_circle.radius}")

    # Автоматический запуск тестов доктеста
    import doctest
    print("\\nЗапуск тестов...")
    doctest.testmod(verbose=True)
