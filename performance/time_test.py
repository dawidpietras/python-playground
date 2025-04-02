import time
import functools

def count_time(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        stop = time.perf_counter()
        elapsed_time = (stop - start)
        print(f"{elapsed_time:.5f} seconds")
    return wrapper

@count_time
def a(lista:list):
    functools.reduce(lambda x, y: x+y, lista)
    
@count_time
def b(lista:list):
    sum(lista)

# a([1]*10**8)
# b([1]*10**8)
a = 17
print(f"{a:07.2f}")