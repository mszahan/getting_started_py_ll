def handle_exception(func):
    def wrapper(*args):
        try:
            func(*args)
        except TypeError:
            print('There was a type error')
        except ZeroDivisionError:
            print('there was zero division error')
        except Exception:
            print('There was some sort of error')
    return wrapper


## now we can use handle_exception as decorator

# @handle_exception
# def cause_error():
#     return 1/0

# cause_error()

@handle_exception
def raise_error(n):
    if n == 0:
        raise Exception()
    print(n)

raise_error(1)