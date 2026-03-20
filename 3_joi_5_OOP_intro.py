import math

class Point:
    def __init__(self, x, y):
       self.x = x
       self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_distance_from_origin(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

Point(5, 12)
print("am un punct la", Point(5, 12))
"am un punct la {}".format(Point(5, 12))
p1 = Point(5, 12)
p2 = Point(5, 12)
p3 = Point(5, 13)
p1 == p2
p1 == p3
p1 != p3
p = Point(5, 12)
p
p.translate(1, 10)
p
Point(5, 12).get_distance_from_origin()
Point(3, 4).get_distance_from_origin()
