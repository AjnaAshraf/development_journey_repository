"""
Common 2D Shapes and Formulas
Rectangle:Multiply length (l) by width (w) (A = l × w)
Square: Multiply the side length (a) by itself (A = a²)
Circle: Multiply pi (π) by the radius squared (A = π r²)
Parallelogram: Multiply base (b) by vertical height (h) (A = bh).
Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two (\(A = \frac{1}{2}(a + b)h\)).
"""

class Shapes:

    name:str

    def __init__(self,name):

        self.name=name

class Parallelogram(Shapes):

    base:int
    height:int

    def __init__(self,name,base,height):

        super().__init__(name) # calling parent class constructor 
        self.base=base
        self.height=height

    def area(self):

        print("area of",self.name, "=",self.base * self.height)

p_instance = Parallelogram("Parallelogram",12,15)
p_instance.area()

class Rectangle(Shapes):

    length:int
    width:int

    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width

    def area(self):

        print("area of ",self.name,"=",self.length * self.width)

rectangle_instance = Rectangle("Rectangle",5,6)
rectangle_instance.area()

class Square(Shapes):

    length:int

    def __init__(self, name,length):
        super().__init__(name)
        self.length=length

    def area(self):

        print("area of ",self.name,"=",self.length**2)

square_instance = Square("Square",5)
square_instance.area()

class Circle(Shapes):

    radius:int

    def __init__(self, name,radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        print("area of ",self.name,"=",3.14 * self.radius**2)

circle_instance = Circle("circle",5)
circle_instance.area()

#Trapezium: Add parallel sides (a + b), multiply by height (h), and divide by two

class Trapezium(Shapes):

    a:int
    b:int
    height:int

    def __init__(self, name,a,b,height):
        super().__init__(name)
        self.a=a
        self.b=b
        self.height=height

    def area(self):

        print("area of ",self.name,"=",((self.a+self.b)*self.height)/2)

trapezium_instance = Trapezium("Trapezium",4,4,5)
trapezium_instance.area()      

    