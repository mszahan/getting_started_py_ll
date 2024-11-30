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

###----------------------------
## class inheritance
###--------------------------

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: yup yup yup')

    def wagtail(slef):
        print('wagging!')

dog = Chihuahua('Roxy')
dog.speak()
dog.wagtail()


##making your own class
class UniqueList(list):
    ## this init overrides everything from the original class
    ## to avoid that you need to add super init within it
    def __init__(self):
        ## add this line to override everything
        ## so this gives parent construtor plus your new property
        super().__init__()
        self.something = 'someting'

    def append(self, item):
        if item in self:
            return
        # # this is calling the append function just defined
        # # not the orginal one from the main function
        # self.append(item)
        super().append(item)


my_list = UniqueList()
my_list.append(1)
my_list.append(1)
my_list.append(2)

print(my_list)

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

# print(wordset.words)

