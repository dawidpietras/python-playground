import functools

def count_time(func):
    "Decorator to count the time of a function"
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed_time = (stop - start)
        print(f"{elapsed_time:.5f} seconds")
    return wrapper

###################################################################################################
"""
Compare the performance of sum and reduce.
Seems like reduce is 10x slower than sum.
sum is a built-in function in Python that is optimized for performance.
reduce is a higher-order function that applies a function cumulatively to the items of an iterable.

"""


@count_time
def reduce_performance(lista:list):
    functools.reduce(lambda x, y: x+y, lista)
    
@count_time
def sum_performance(lista:list):
    sum(lista)

"""
test_list = [1]*10**8

reduce_performance(test_list)
# 5.26 s

sum_performance(test_list)
# 0.48 s
"""

##################################################################################################