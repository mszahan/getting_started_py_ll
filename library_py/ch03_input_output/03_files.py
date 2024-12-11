my_file = open('score.txt', 'w')


## show attributes and properties of the file

print('Name', my_file.name)
print('Mode', my_file.mode)


## write to the file
my_file.write('alex: 100,\n Rebecca: 95 \n angel: 49')
## closing files also reset the seek point to 0
my_file.close()


## read the file
my_file = open('score.txt', 'r')
# print('Reading...', my_file.read())
## you can read 10 char like this
print('Reading...', my_file.read(10))
my_file.seek(0)
## reading from the beginning again with seek setting to 0
print('Reading from beggining again', my_file.read(20))

