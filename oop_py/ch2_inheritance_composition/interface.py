from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()
    ## abstractmethod has to be instantiate by every subclass method
    @abstractmethod
    def calc_area(self):
        pass

## I think this is called interface
class JSONify(ABC):
    @abstractmethod
    def to_json(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius
    
    def calc_area(self):
        return 3.14 * (self.radius ** 2)

    def to_json(self):
        return f'{{"Circle": {str(self.calc_area())}}}'
    

## ABC can't be called like that- you can't use this
# g = GraphicShape()


c = Circle(10)
print(c.calc_area())

print(c.to_json())

