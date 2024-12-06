## least to greatest
points = [0, -10, 15, -2, 1, 12]
sorted_points = sorted(points)

print('not sorted', points)
print('not sorted', sorted_points)


## Alphabetically
children = ['Sue', 'Jerry', 'Linda']
print(sorted(children))


## key parameters
print(sorted(children, key=str.upper))
print(sorted(points, reverse=True))