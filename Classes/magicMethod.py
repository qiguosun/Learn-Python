class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # overide print magic functions
        return f"{self.x},{self.y}"

    def draw(self):
        print(f"Point ({self.x},{self.y})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(1, 4)
other = Point(1, 4)
print(point)
print(point == other)
print(point+other)
