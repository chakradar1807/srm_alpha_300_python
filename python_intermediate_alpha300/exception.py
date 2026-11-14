class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)



import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this ia a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')


import random

mylist = list("ABCDEFGH")
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(3,10))


import secrets

alist = list("ABCDEFGHIJK")
a = secrets.choice(alist)
print(a)



import numpy as np

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():
    print('Alex')

print_name()

    
def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5



import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')
greet('Alex')


class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'this is executed{self.num_calls} times')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('hello')

say_hello()
say_hello()

def mygenerator():
    yield 1
    yield 2
    yield 3
g = mygenerator()

print(sorted(g))

def countdown(num):
    print('starting')
    while num > 0:
        yield num
        num -=1

cd = countdown(4)

value = next(cd)
print(value)

print(next(cd))


def first(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn_generator(10)))
print(sum(firstn_generator(10)))            


def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b
fib = fibonacci(30)
for i in fib:
    print(i)        


import sys
mygenerator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range(1000000) if i % 2 == 0]
print(sys.getsizeof(mylist))