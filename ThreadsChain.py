import threading

count = 0
def threadMake(count):
    if count < 50:
        count += 1
        t = threading.Thread(target=threadMake, args=(count,))
        t.start()
        print('Hello from Thread ', count)
t = threading.Thread(target=threadMake, args=(count,))
t.start()
