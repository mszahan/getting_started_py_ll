from random import randint
from collections import Counter


def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((randint(1, sides) for sides in dice))] +=1

    print('\nOUTCOME\tPROBABILITY')
    for outcom in range(len(dice), sum(dice) + 1):
        print(f'{outcom} \t {counts[outcom] *100 / num_trials : .2f}%')
## chcked the probability of one 4 sided dice and two 6 sided dice
roll_dice(4, 6, 6)