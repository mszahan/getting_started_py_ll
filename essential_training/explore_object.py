class Dog:
    # static variable
    _legs = 4
    def __init__(self, name):
        self.name = name
        # self.legs = 4
    
    # its best practice to get the static variable in get function
    def get_legs(self):
        return self._legs

    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog('Rover')
# print(my_dog.name)
# print(my_dog.legs)
# my_dog.speak()

# print(Dog._legs)
# print(my_dog.get_legs())

###______------------------------------
## Static and instance methods
#############--------------------------

class WordSet:
    replace_punc = ['!', '.' ',' '\'']
    def __init__(self):
        self.words = set()
    
    #this is intance method
    def add_text(self, text):
        # text = self.clean_text(text)
        # text = WordSet.clean_text(text)
        ## after the static method we can again use self
        text = self.clean_text(text)
        for word in text.split():
            self.words.add(word)

    #this is static method that doesn't require self
    #we can get rid of the self
    # def clean_text(self, text):
    ## we can use decorator to use it without calling WordSet main class
    @staticmethod
    def clean_text(text):
        # text = text.replace('!', '').replace('.', '').replace(',', '').replace('\'', '')
        for punc in WordSet.replace_punc:
            text = text.replace(punc, '')
        return text.lower()


wordset = WordSet()

wordset.add_text('Hi, I\'m Ryan! Here is the sentence I want to add!')
wordset.add_text('Here is another sentence I want to add.')

print(wordset.words)

