import time

run = input('start ? \n> ')

seconds = 0

if run == 'yes':
    while seconds !=10:
        print('>', seconds)
        time.sleep(1)
        seconds +=1

