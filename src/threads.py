import threading
import time

def slowSquare(num, results):
    time.sleep(2)
    results[num] = num ** 2

results = {} # used to store result of computation done by a thread
threads = [threading.Thread(target=slowSquare, args=(num, results)) for num in range(1, 100)]
[t.start() for t in threads]
[t.join() for t in threads]

print(sorted(results.values()))
