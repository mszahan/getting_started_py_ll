import itertools

## permutations

election = {1: 'Barb', 2:'Karen', 3:'Erin'}

## now we can get all the possible permutations in this way
for p in itertools.permutations(election):
    print(p)

for p1 in itertools.permutations(election.values()):
    print(p1)



## combination

painting_colors = ['red', 'blue', 'purple', 'orange', 'yellow', 'pink']

## now creating combinations with 2 value each
for c in itertools.combinations(painting_colors, 2):
    print(c)
    