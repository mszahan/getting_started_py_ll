
## create basic class
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    
    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'
    
    ## when the atribute price is called we want to implement the discount autmaticallyy
    def __getattribute__(self, name):
        if name == 'price':
            p = super().__getattribute__('price')
            d = super().__getattribute__('_discount')
            return p - (p*d)
        #  if price is not called, then this line will return whatever attribute called
        return super().__getattribute__(name)

    ## we can set attribute to make it follow certain rule
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError('The price attr must be float')
        return super().__setattr__(name, value)
    
    ## checking get_attr
    ## it execute if getattibute doesn't work or called
    def __getattr__(self, name):
        return name + ' is not here'
    

    
    

## create instance of the class
book1 = Book('Atomic habit', 'james clear', 50.5)
book2 = Book('Rich dad poor dad', 'robert kyosaki', 23.3)
book3 = Book('Atomic habit', 'james clear', 50.5)
book4 = Book('To kill a Mockingbird', 'Harper Lee', 24.95)

## now we are callig the price attribute
## so it will return afer dicounted price
book1.price = 30.25 # set price to be float only
print(book1.randoprop)

