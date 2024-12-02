
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        # self.title = title
        self.author = author
        self.pages = pages
        # self.price = price


class Magazine(Periodical):
    def __init__ (self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        # self.title = title
        # self.publisher = publisher
        # self.price = price
        # self.period = period
    

class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)
        # self.title = title
        # self.price = price
        # self.period = period
        # self.publisher = publisher


b1 = Book('Rich dad poor dad', 'Robert', 320, 110)
n1 = Newspaper('WSJ', 'Wall street Journal publication', 6, 'Daily')
m1 = Magazine('Scientific American', 'Springer Nature', 5.99, 'Monthly')

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)