from math import sqrt


class Point:
    """
    Point with x,y coordinates
    """
    def __init__(self, x: float, y: float) -> None:
        """
        Initialisation a point with x,y coordinates
        :param x: x-coordinate of the point
        :param y: y-coordinate of the point
        """
        self.x = x
        self.y = y


class Circle:
    """
    Geometric figure circle
    """
    def __init__(self, x: float, y: float, radius: float) -> None:
        """
        Initialisation a circle with center in x,y coordinates and radius
        :param x: x-coordinate of center
        :param y: y-coordinate of center
        :param radius: radius of circle
        """
        self.x = x
        self.y = y
        self.radius = radius

    def __contains__(self, point: Point) -> bool:
        """
        Redefine __contains__ method
        Check if point is inside circle
        If distance between radius and center <= radius then point is inside circle else point is outside
        Distance = sqrt (x1 - x2) ** 2 + (y1 - y2) ** 2
        :param point: instance of Point with x,y coordinates
        :return: True if point is inside else False
        """
        distance = sqrt(abs((point.x - self.x) ** 2 + (point.y - self.y) ** 2))
        return distance <= self.radius


my_circle = Circle(0, 0, 10)
my_point1 = Point(0, 10)
my_point2 = Point(0, 11)

print(my_point1 in my_circle)
print(my_point2 in my_circle)
