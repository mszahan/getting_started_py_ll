from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author: str
    pages : int
    price : float

    ## after the object has been initialized via built-in __init__
    ## if you need some customized atribute you can use __post_init__
    def __post_init__(self):
        self.description = f'{self.title} by {self.author}, {self.pages} pages'

    
    
## create instance of the class
book1 = Book('Atomic habit', 'james clear', 540,  50.30)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 350, 23.3)

## Print the class and property

# print(book1.title)
# print(book2.author)

print(book1.description)
print(book2.description)