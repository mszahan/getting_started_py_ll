animals = [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]

animal_dict = {item[0]: item[1] for item in animals}
# the elegant way of coding the same line
# animal_dict = {key: value for key, value in animals}
print(animal_dict)

# reversing the dictionary to list again
new_animals = list(animal_dict.items())