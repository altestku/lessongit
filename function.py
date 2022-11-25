# import functools
from functools import *


def sum_arr(arr1, arr2):
    return reduce(lambda x, y: x+y, arr1 + arr2)

def avarage_arr(arr):
     return sum(arr)/len(arr) if len(arr) > 0 else 0
    # return filter(lamda x:)



