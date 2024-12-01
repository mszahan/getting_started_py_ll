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


###-----------------
## Creating custom exception class with attribute
####---------------

class HttpException(Exception):
    status_code = None
    message = None
    def __init__(self):
        super().__init__(f'Status code: {self.status_code} and message is {self.message}')
    

class NotFound(HttpException):
    status_code = 404
    message = 'Resource not found'

class ServerError(HttpException):
    status_code = 500
    message = 'The server messed up'


def raise_server_error():
    raise ServerError()

raise_server_error()