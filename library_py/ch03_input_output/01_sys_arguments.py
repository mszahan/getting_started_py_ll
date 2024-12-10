import sys


## remove arguments
sys.argv.remove(sys.argv[0])


##print command line argument
print('number of arguments', len(sys.argv), 'arguments')

## the file name is the default argument
print('arguments', sys.argv)

arguments = sys.argv
sum = 0

for arg in arguments:
    try:
        number = int(arg)
        sum += number

    except Exception:
        print('Bad input')


print('sum of all the argument is ', sum)