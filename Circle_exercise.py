class Circle:
    pi = 3.14 #class object attribute
    def __int__(self,radius):
        self.radius=radius
        self.area=Circle.pi * radius * radius
    def get_circumference(self):
        return 2 * Circle.pi * self.radius

circle_1 = Circle(4)
print(circle_1.get_circumference())
circle_2 = Circle(14)
print(circle_2.get_circumference())
print(circle_1.area)