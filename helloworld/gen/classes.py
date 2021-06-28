# https://rszalski.github.io/magicmethods/
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "Yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

zpoint = Point.zero()
print(str(zpoint))

combined = point + another
print(combined)
