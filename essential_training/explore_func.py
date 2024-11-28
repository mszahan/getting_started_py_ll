import math
# # if you nedd to pass any number of argument use *args
# # args gives you a tuple

# def display_args(*args):
#     print(args)

# display_args(1,2,4)


# # if you need to pass any number of keyword arguments use **kwargs
# # it gives you a dictionary
# def display_kwarg(**kwargs):
#     print(kwargs)

# display_kwarg(hola='hello', run=False, num=2)


def perform_operation(*args, opeartions='sum'):
    if opeartions == 'sum':
        return sum(args)
    if opeartions == 'multiply':
        return math.prod(args)
    

print(perform_operation(4,6,8,9))