from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    ## you can give default value in dataclass like this
    ##*** very important atribute that doesn't have defult value need to come first
    title : str = 'no title'
    author: str = 'no author'
    pages : int = 0
    # price : float = 0.0
    ## let's do this way for advantage
    # price : float = field(default=10.0)
    ## now we will paass function for default price
    price : float = field(default_factory=price_func)


# b1 = Book()
# print(b1)

book1 = Book('Atomic habit', 'james clear', 540 )
book2 = Book('Rich dad poor dad', 'robert kyosaki', 350 )


print(book1)
print(book2)
