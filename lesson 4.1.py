from function import *

# arr1 = [1, 2, 4, 6]
# arr2 = [6, 7, 8, 8, 9]
#
# print(sum_arr(arr1, arr2))
#
# arr3 = [1, 4, 5, 7, 9, 8]
# print(round(avarage_arr(arr3),2))

x = 3
def new_one():
    x = 2
    print(f'inner:{x}')

print(f'output:{x}')
new_one()
print(f'output:{x}')