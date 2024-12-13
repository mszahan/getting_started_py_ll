set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

## union of the set
union_set = set_A.union(set_B)
print(union_set)

## intersection
intersection_set = set_A.intersection(set_B)
print(intersection_set)

## difference is the subtract of the sets
difference_set = set_A.difference(set_B)
print(difference_set)

## let's try reverse
reverse_subtract = set_B.difference(set_A)
print(reverse_subtract)

## symetric difference is the unique to both
symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set)