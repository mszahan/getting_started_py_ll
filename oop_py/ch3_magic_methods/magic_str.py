
## create basic class
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f'{self.title} by  {self.author}, costs {self.price} \n'
    
    def __repr__(self):
        return f'title={self.title}, author={self.author}, price={self.price}'

## create instance of the class
book1 = Book('Atomic habit', 'james clear', 50.5)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 23.3)

## Print the class and property

print(book1)
print(book2)

print(str(book1))
print(repr(book1))