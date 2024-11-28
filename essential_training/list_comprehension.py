#list comprehension with filter
my_list = list(range(100))
filtered_list = [item for item in my_list if item % 10 == 0]

print(filtered_list)


# list comprehension with function
my_string = 'My name is Sarwar. I live in Chapai'
# my_string.split()

def clear_word(word):
    return word.replace('.', '').lower()

cleaned_word = [clear_word(word) for word in my_string.split()]
print(cleaned_word)

#nested list comprehension
nested = [[clear_word(word) for word in sentence.split()] for sentence in my_string.split('.')]
print(nested)