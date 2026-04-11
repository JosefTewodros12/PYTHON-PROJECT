class Recatangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length + self.width)


r1 = Recatangle(10, 20)
print(r1.area())
print(r1.perimeter())
