import math
from sympy import Point
from ex12_point2d import Point2D


class Vector2D(object):
    """
    Vecteur dans un plan
    >>> O = Point2D()
    >>> A = Point2D(1, 0)
    >>> B = Point2D(1, 1)
    >>> C = Point2D(0, 1)
    >>> v1 = Vector2D(O, A)
    >>> v2 = Vector2D(O, B)
    >>> v3 = Vector2D(O, C)
    >>> print(v1)
    Vector2D(1,0)
    >>> print(v2)
    Vector2D(1,1)
    >>> print(v3)
    Vector2D(0,1)
    >>> print(abs(v1))
    1.0
    >>> print(abs(v2))
    1.4142135623730951
    >>> print(-v1)
    Vector2D(-1,0)
    >>> print(v1 + v2)
    Vector2D(2,1)
    >>> print(v1 + v3)
    Vector2D(1,1)
    >>> print(v1 - v3)
    Vector2D(1,-1)
    >>> print(v1 + v3 == v2)
    True
    """

    def __init__(self, p1=Point2D(0, 0), p2=Point2D(0, 0)):
        self.x = p2.x - p1.x
        self.y = p2.y - p1.y

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return "Vector2D({},{})".format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        result = Vector2D()
        result.x = -self.x
        result.y = -self.y
        return result

    def __add__(self, other):
        result = Vector2D()
        result.x = self.x + other.x
        result.y = self.y + other.y
        return result

    def __sub__(self, other):
        result = Vector2D()
        result.x = self.x - other.x
        result.y = self.y - other.y
        return result


def main():
    O = Point2D()
    A = Point2D(1, 0)
    B = Point2D(1, 1)
    C = Point2D(0, 1)
    v1 = Vector2D(O, A)
    v2 = Vector2D(O, B)
    v3 = Vector2D(O, C)
    print(v1)
    print(v2)
    print(v3)
    print()
    print(abs(v1))
    print(-v1)
    print(v1 + v2)
    print(v1 + v3)
    print(v1 - v3)
    print(v1 + v3 == v2)


if __name__ == "__main__":
    main()
