class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
     

    def perimeter(self):
        return 2 * 3.14 * self.radius 

radius = float(input("enter the radius: "))

c = circle(radius)

print("Area =", c.area())
print("Perimeter =", c.perimeter())