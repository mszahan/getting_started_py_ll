
## create basic class
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

        ## eq method checks for equality
        ## now if the conditions are true the instance will be equal
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Cannot compare book to a non-book')
        return (self.title == value.title and self.author == value.author and
                self.price == value.price)
    
    ## checking greater than equal to with price only
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Cannot compare book to a non book')
        return self.price >= value.price
    
    ## checking less than equal to with price only
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError('Cannot compare book to a non book')
        return self.price < value.price
    
    
    

## create instance of the class
book1 = Book('Atomic habit', 'james clear', 50.5)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 23.3)
book3 = Book('Atomic habit', 'james clear', 50.5)
book4 = Book('To kill a Mockingbird', 'Harper Lee', 24.95)

## check equality
print(book1 == book3)
print(book1 == book2)

## check lesser or greater
print(book2 >= book1)
print(book2 < book1)

## now you can sort the books

books = [ book1, book3, book2, book4]
books.sort()
print([book.title for book in books])
