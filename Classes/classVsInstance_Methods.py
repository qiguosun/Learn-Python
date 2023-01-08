# instance method vs class method
# class-level method: such as get a (0,0) point use Point.zero()
# define a factory method
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  # this is a decorator, a class-level method
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x},{self.y})")


point = Point.zero()
point.draw()
