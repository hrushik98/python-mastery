import time

#Decorators are useful in many situations
#where you want to modify the behavior of a function or class without changing its source code.

# Timing and profiling: You can use a decorator to time how long a function takes to run, or to profile its performance.

# Caching: You can use a decorator to cache the results of a function so that it doesn't have to be recomputed every time it's called.

# Authentication and authorization: You can use a decorator to check if a user is authenticated or authorized to access a particular resource.

# Logging: You can use a decorator to log information about a function's inputs, outputs, and exceptions.

# Validation: You can use a decorator to validate the inputs and outputs of a function, or to enforce certain constraints on its behavior.

# Retry and error handling: You can use a decorator to automatically retry a function if it fails, or to handle errors in a specific way.

# Memoization: You can use a decorator to memoize a function, which means that it will remember the results of previous calls and return them instead of recomputing them.

def calc_time(func):
    def wrapper():
        t = time.time()
        func()
        total_time = time.time()- t
        print(f"{func.__name__} took {total_time} seconds to run.")
    return wrapper 




@calc_time
def print_hi():
    time.sleep(2)
    print("Hi!")

@calc_time
def print_hello():
    time.sleep(1)
    print("Hello!")

print_hi()

