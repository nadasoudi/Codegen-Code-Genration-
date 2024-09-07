def time_since_startup(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Finished {func.__name__} in {end - start:.2f} seconds")
        return result
    return wrapper

@time_since_startup
def display_hi():
    print("Hello from the function")

display_hi()

"""

#