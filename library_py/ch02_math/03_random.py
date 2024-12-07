import random


## random numbers
print(random.random()) # prints random number between 0 and 1

print(random.randrange(3)) # it works like range but random

decider = random.randrange(2)
if decider == 0:
    print('HEADS')
else:
    print('TAILS')

print('your roled the dice and it is ', random.randrange(1, 7))



## random choices

## if you need 5 random number in a range you can do this way
lottery_winners = random.sample(range(100), 5)
print('The winners are', lottery_winners)

## now select the choices
possible_pets = ['cat', 'dog', 'fish']
print(random.choice(possible_pets))

## now let's suffle the cards
cards = ['Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)