import time
import threading

def long_square(num, results):
    time.sleep(1)
    results[num] = num**2

results = {}
# t1 = threading.Thread(target=long_square, args=(1, results))
# t2 = threading.Thread(target=long_square, args=(2, results))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

## doing it in loop

threads = [threading.Thread(target=long_square, args=(n, results)) for n in range(0,10)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)

