import time

def func_time(func):
    def wrapper(text):
        start = time.time()
        func(text)
        end = time.time()
        elapsed = end - start
        print(f"A function {func.__name__} executed in {elapsed:.4f} seconds")
    return wrapper