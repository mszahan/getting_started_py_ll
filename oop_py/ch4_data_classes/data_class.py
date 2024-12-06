from dataclasses import dataclass

## create basic class
# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price


## now let's convert this object with dataclass

@dataclass
class Book:
    title : str
    author: str
    pages : int
    price : float

    def bookinfo(self):
        return f'{self.title} by {self.author}'
    
## create instance of the class
book1 = Book('Atomic habit', 'james clear', 540,  50.30)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 350, 23.3)
book3 = Book('Atomic habit', 'james clear', 540,  50.30)

## Print the class and property

# print(book1.title)
# print(book2.author)

##dataclass method already implements repr and eq functions
# print(book1 == book3)
# print(book1 == book2)
# print(book1)


## modify the some atribute
book1.title = 'Anna Karenina'
book1.author = 'Not james clear'
print(book1.bookinfo())
