import threading 
import time 

numbers = [1,2,3,4]

def square(numbers):
    for number in numbers:
        print('square:', number * number)
        time.sleep(1)

def cube(numbers):
    for number in numbers:
        print('cube:', number * number * number)
        time.sleep(1)

t1 = threading.Thread(target = square, args=(numbers,) ) #since it is a tuple put (,) at the end
t2 = threading.Thread(target = cube, args=(numbers,) )

t = time.time()

t1.start()
t2.start() 

t1.join()
t2.join()

print('Done!')

print(time.time() - t)