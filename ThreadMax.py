import random #Maybe I'll get this working at a future date. For now, no time
import threading

def checkValue(value, array,a):
    if value > threadVal:
        threadVal = value
    else:
        array.remove(value)
a = 10
array = range(a)
for i in range(10):
    t = threading.Thread(target=checkValue, args=(value,array,a))
