class Polygon:
    def __init__(self, count_sides, sides):
        self.count_sides = count_sides
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class RegularPolygon(Polygon):
    def __init__(self, count_sides, length):
        super().__init__(count_sides, [length] * count_sides)
        self.length = length

    def area(self):
        import math
        apothem = self.length / (2 * math.tan(math.pi / self.count_sides))
        return (self.perimeter() * apothem) / 2

class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        super().__init__(3, [side1, side2, side3])
        
    def area(self):
        import math
        p = self.perimeter() / 2
        return math.sgrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4, [length, width, length, width])
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

class Square(RegularPolygon):
    def __init__(self, length):
        super().__init__(4, length)

class Trapezius(Polygon):
    def __init__(self, base1, base2, height, leg1, leg2):
        super().__init__(4, [base1, leg1, leg2, base2])
        self.base1 = base1
        self.base2 = base2
        self.height = height
        
    def area(self):
        return ((self.base1 + self.base2) / 2) * self.height

class Parallelogram(Polygon):
    def __init__(self, base, height, side):
        super().__init__(4, [base, side, base, side])
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height
