from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    ## abstractmethod has to be instantiate by every subclass method
    @abstractmethod
    def calc_area(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * (self.radius ** 2)
    

class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calc_area(self):
        return self.side * self.side
    
## ABC can't be called like that- you can't use this
# g = GraphicShape()


c = Circle(10)
print(c.calc_area())
s = Square(12)
print(s.calc_area())

