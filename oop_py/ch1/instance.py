
## create basic class
class Book:
    def __init__(self, title):
        self.title = title


## create instance of the class
book1 = Book('Atomic habit')
book2 = Book('Rich dad poor dad')

## Print the class and property

print(book1)
print(book1.title)
