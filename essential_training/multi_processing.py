from multiprocess import Process
import time


def long_square(num, results):
    time.sleep(1)
    print(num**2)
    print('fininsh computing')
results = {}
processes = [Process(target=long_square, args=(n, results)) for n in range(0,10)]
[p.start() for p in processes]
[p.join() for p in processes]