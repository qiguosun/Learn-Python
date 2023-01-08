# self is a reference to current object
# class level attibutes are shared among all instances (color)

class Point:
    color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point(1, 2)
print(isinstance(point, Point))
print(point.x)
point.draw()
print(point.color)
print(Point.color)

# if change the class level attribute, the instance of this attribute change
Point.color = "Green"
newpoint = Point(1, 3)
print(newpoint.color)
