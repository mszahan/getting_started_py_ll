class Book:
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    __booklist = None

    ## creating a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def set_title(self, newtitle):
        self.title = newtitle
    
    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype
        
print('Book types: ', Book.get_book_types())
    
b1 = Book('rich dad poor dad', 'HARDCOVER')
b2 = Book('atomic habit', 'PAPERBACK')

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
