class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 22/7 * self.radius**2

    def calculate_perimeter(self):
        return 2 * 22/7 * self.radius

radius = int(input("Enter the radius: "))
my_circle = Circle(radius)
area = my_circle.calculate_area()
perimeter = my_circle.calculate_perimeter()

print("Area:", area)
print("Perimeter:", perimeter)
