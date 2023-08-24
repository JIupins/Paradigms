class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Круг")


class Rectangle(Shape):
    def draw(self):
        print("Прямоугольник")


class Triangle(Shape):
    def draw(self):
        print("Треугольник")


class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError("Неизвестный тип фигуры")


factory = ShapeFactory()

circle = factory.create_shape("circle")
circle.draw()

rectangle = factory.create_shape("rectangle")
rectangle.draw()

triangle = factory.create_shape("triangle")
triangle.draw()