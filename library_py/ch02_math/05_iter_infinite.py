import itertools

## infinite counting

for x in itertools.count(50, 5):
    print(x)
    if x == 80:
        break


## Infinite cycling
x = 0
for c in itertools.cycle('Keep repeating the chars'):
    print(c)
    x+=1
    if x > 50:
        break
 

## Infinite Repeating
for r in itertools.repeat(True):
    print(r)
    x+=1
    if x >100:
        break

