
## create basic class
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        ## properties with double underscore are hidden
        ## and not accessible by the instance
        self.__secret = 'this is secret attribute'

    ## create instance method
    def getprice(self):
        ## since it might not exists so to check is necessary
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        ## this underscore is to say this variable is internal to class
        self._discount = amount


## create instance of the class
book1 = Book('Atomic habit', 'James clear', 325, 120)
book2 = Book('Rich dad poor dad', 'Robert', 250, 110)

## Print the class and property
print(book1.getprice())
print(book2.getprice())
book2.setdiscount(0.25)
print(f'after discount price {book2.getprice()}')

## this atribute is not accessible it gives error
# print(book2.__secret)
## though you can access the following way
print(book2._Book__secret)