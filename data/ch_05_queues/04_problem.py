## return binary number
from collections import deque

def print_binary_numbers(n):
    if n <=0:
        return
    
    queue = deque()
    queue.append(1)

    for i in range(n):
        binary = queue.popleft()
        print(binary)
        ## this is to add zero
        queue.append(binary * 10)
        ## to add 1 at the end
        queue.append(binary * 10 + 1)


print(print_binary_numbers(6))
