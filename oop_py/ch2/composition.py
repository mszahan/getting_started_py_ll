class Book:
    def __init__(self, title, price, author=None):
        self.title = title
        self.price = price
        
        # self.authorfname = authorfname
        # self.authorlname = authorlname
        self.author = author

        self.chapters = []
    
    # def addchapter(self, name, pages):
    #     self.chapters.append((name, pages))
    def addchapter(self, chapter):
        self.chapters.append((chapter))

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result
    



class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
    

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount




# b1 = Book('Rich dad poor dad', 110, 'Robert', 'Kiyosaki')
auth = Author('Robert', 'Kiyosaki')
b1 = Book('Rich dad poor dad', 110, auth)

b1.addchapter(Chapter('chapter 1', 125))
b1.addchapter(Chapter('chapter 2', 97))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())