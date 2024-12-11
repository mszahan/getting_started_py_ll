my_file = open('score.txt', 'r')


## read one line
print('read one line \n', my_file.readline())
my_file.seek(0)

## iterate through 
for line in my_file:
    ## it's not changing the file since it's one reading mode
    ## just changing the variable change_name
    change_name = line.replace('angel', 'Angell')
    print(change_name)
my_file.close()
