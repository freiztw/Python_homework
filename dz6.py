# func = lambda x = int(input("Введите число: ")): print("четное") if x % 2 == 0 else print("нечетное")
# func()

#
# list_numbers = [1, 3, 65, -6]
# str_numbers = list(map(lambda x: str(x), list_numbers))
# print(str_numbers)


# polindrom = ('ababa', 'lal', '121')
# pr1 = tuple(filter(lambda x: x == x[::-1], polindrom))
# print(pr1)





from functools import wraps
from typing import Callable
from datetime import datetime

#
#
#
# def decorator(func: Callable) -> Callable:
#     @wraps(func)
#     def inner(*args, **kwargs):
#         before_time = datetime.now()
#         result_time = func(*args, **kwargs)
#         after_time = datetime.now()
#         print(f' результат = {result_time}, время выполнения = { after_time - before_time}')
#
#         return result_time
#     return inner
#
# @decorator
# def func(a: int, b: int) -> int:
#     result = (a + b)*b - (a ** b) - a**a
#     return result
#
# func(1, 2)
#
# @decorator
# def func1(a: int, b: int) -> int:
#     result = (a + b)*b - (a ** b) - a**a
#     return result
#
# func(11, 15)