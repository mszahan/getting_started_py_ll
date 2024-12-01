class Book:
    def __init__(self, title):
        self.title = title



class Newspaper:
    def __init__(self, name):
        self.name = name

b1 = Book('Rich dad poor dad')
b2 = Book('Blink')
n1 = Newspaper('The Gurdian')
n2 = Newspaper('Wall street Journal')

# checking types of the instances
print(type(b1))
print(type(n1))

## use isinstance to compare a specific instance to a known type

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
