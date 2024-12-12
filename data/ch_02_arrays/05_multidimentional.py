seating_chart = [
    ['Sarah', 'Claire', 'Ben', 'Taylor', 'Eva'],
    ['Frankie', 'George', 'Lindsey', 'Izzy', 'Jack'],
    ['Katherine', 'Lauren', 'Mary', 'Nathan', 'Olive'],
    ['Chad', 'April', 'Matt', 'Thomas', 'Penny']
]

## enumarate give you index and value of list
for i, row in enumerate(seating_chart):
    for j, student in enumerate(row):
        print(f'{student} is in row {i+1}, seat {j+1}')


