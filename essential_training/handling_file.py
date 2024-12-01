## reading a file
# f = open('text.txt', 'r')

## reading one line
# print(f.readline())

## reading all the lines
# print(f.readlines())

## reading file in a loop line by line
# for line in f.readlines():
#     #get rid of extral new line
#     print(line.strip())

## opeing in writing mode
# f = open('text2.txt', 'w')

# f.write('this is line one')
# f.write('this is line 2')
# f.close()

## opening in appending method

with open('text2.txt', 'a') as f:
    f.write('this is line 2 \n')
    f.write('this is line 3 \n')