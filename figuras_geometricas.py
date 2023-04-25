from math import pi, sqrt

class Shape:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def get_area(self):
        return self.side1 * self.side2

    def __str__(self):
        return f'The area of this {self.__class__.__name__} is: {self.get_area()}'


class Rectangle(Shape):
    pass


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Rectangle):
    def __init__(self, height, base):
        super().__init__(height, base)

    def get_area(self):
        area = super().get_area()
        return area / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = (self.radius ** 2) * pi
        return area


class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * sqrt(3) * self.side ** 2) / 2


class Run:
    def __init__(self):
        pass

    def run():
        print("Which Shape size do you want to calculate? 1. Rectangle 2. Square 3. Triangle 4. Circle 5. Hexagon 6. Exit")
        selection = int(input("Please select: "))

        if selection == 1:
            side1 = float(input("Enter side1 of Rectangle: "))
            side2 = float(input("Enter side2 of Rectangle: "))
            print(Rectangle(side1, side2))

        elif selection == 2:
            side = float(input("Enter side of Square: "))
            print(Square(side))

        elif selection == 3:
            base = float(input("Enter base of Triangle: "))
            height = float(input("Enter height of Triangle: "))
            print(Triangle(base, height))

        elif selection == 4:
            radius = float(input("Enter radius of Circle: "))
            print(Circle(radius).__str__())

        elif selection == 5:
            side = float(input("Enter side of Hexagon: "))
            print(Hexagon(side))

        elif selection == 6:
            exit("Exiting")

        else:
            exit("Please select between 1-6, exiting")


Run.run()