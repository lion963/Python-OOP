def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())


def print_message(message):
    def message_sender():
        "Nested Function"
        print(message)
    message_sender()

print_message("Some random message")


def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper


def say_hi():
    return 'hello there'

decorate = uppercase(say_hi)
print(decorate())


def uppercase(function):
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

@uppercase
def say_hi():
    return 'hello there'
print(say_hi())


from time import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        end = time()
        print(end - start)
        return func(*args, **kwargs)
    return wrapper


@measure_time
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(4)
def say_hi():
    print("Hello")

say_hi()


class Fibonacci:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self(n-1) + self(n-2)
        return self.cache[n]


fib = Fibonacci()

for i in range(5):
    print(fib(i))

print(fib.cache)

class func_logger:

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.func(*args)

@func_logger
def say_hi(name):
    print(f"Hi, {name}")

@func_logger
def say_bye(name):
    print(f"Bye, {name}")

say_hi("Peter")
say_bye("Peter")
