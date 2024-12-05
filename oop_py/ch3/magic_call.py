
## create basic class
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f'{self.title} by  {self.author}, costs {self.price} \n'
    
    ## the call method can be used to call the object like function
    def __call__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price

## create instance of the class
book1 = Book('Atomic habit', 'james clear', 50.5)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 23.3)

print(book1)
## now you can change the object like function
book1('Anna Karenina', 'Leo tolstoy', 49.95)
print(book1)