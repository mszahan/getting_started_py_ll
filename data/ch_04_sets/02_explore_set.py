primary_color = set(['red', 'blue', 'yellow'])

color = 'green'

if color in primary_color:
    print(color, 'is a primary color')
else:
    print(color, 'is not a primary color')

## adding new element to set
## set doesn't have index (fixed position for elements) like dictionary
## set doesn't contain duplicate value
letters = set(['a', 'b'])
letters.add('c')
print(letters)