# l=[]
# print(l)
# l = [1,'string',12.3, 'hello', 25]
# print(l)

# sentence = 'What a wonderful life'
# my_list = list(sentence)
# print(my_list)
# my_list1 = sentence.split(' ')
# print(my_list1)
# print(my_list1[0])
#
# my_list.append('!')
# print(my_list)

# l = [8, 7, 5, 10]
# print(l)
# print(id(l))
# l[0]=0
# print(l)
# print(id(l))

# l1 = [25,80]
# add='extra'
# l.append(add)
# l.extend(add)
# print(l)
# print(id(l))

# nums = [2, 3, 1, 5, 6, 4, 0]
# print(f'initial list:{(nums)}')
# print(id(nums))
# print('sorted()')
# print(f'new sorted list:{sorted(nums)}')
# print(f'initial list after sorting:{nums}')
#
# print('.sort()')
# print(f' new sorted list:{nums.sort()}')
# print(f' initial list after sorting: {nums}')
# print(id(nums))
# print(nums.reverse())
# print(nums)
# print(id(nums))
# print(nums.reverse())
# print(nums)
# prin


# letters = ['a', 'b', 'c', 'd', 'e','f']
# print(letters[0:-1:2])
# print (letters[::-1])

# l=[1, 2, 3, 4, 5]
# new_l=[x*x for x in l if x%2]
# print (new_l)

# str = 'cdjshjfj123'
# print(sorted(str, reverse = True))


# mytuple =(1, True, 'name' , None, 'name',24)
# print (mytuple)

# name=('MARK')
# print(name)
# print (type(name))

# letters = ('apple', 'banana', 'cat')
# a, b , c = letters
# print(a, b, c)

# letters[0] = 'ananas'
# print (letters)

# letters = list(letters)
# letters[0] = 'ananas'
# print (letters)

# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple (filter (lambda x : isinstance(x, int), my_tuple))
# print(result)
# #
# my_tuple = (1, True, 'name', None, 'name', 25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))


# print(f'Sum is:{sum(result)}')
# print(f'Max is:{max(result)}')
# print (f'Length of my tuple is: {len(my_tuple)}')

# for (index, item) in enumerate(my_tuple):
#     print(index,item)

# i = 0
# while i < len(my_tuple):
#     print(my_tuple[i])
#     i+=1

# letters = ('apple', ['ananas', 'mango'], 'melon')
# letters[1][0] = 'cherry'
# print(letters)

# a = 5
# b = 10
# a, b = b, a
# print(f'a={a}')
# print(f'b={b}')

# def sum_it(*args):
#     total = 0
#     for num in args:
#        total = total +num
#     return total
# print(sum_it(4, 5, 10, 6, 20))


# def func(*args):
#     l =[]
#     for item in args:
#         l.append(item*item)
#     return l
# print(func(2, 5, 6, 8, 10, 16))

# my_dict = {
#     'name':'Anna',
#     'last_name': 'Pavlova',
#     'age': 30,
#     'department': 'IT'


# print(my_dict)
# print(my_dict['name'])
# my_dict['last_name'] ='smirnova'
# # print(id(my_dict))
# print(my_dict)
# print(id(my_dict))
# print(len(my_dict))
# my_dict['salary'] = 5000
# print(my_dict)
# print(len(my_dict))
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary', 'Not found'))

# print(set([1, 8, 2, 1, 5, 8,9]))

# set1 = {1, 2, 3, 'one', 'two'}
# set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}
#
# print(set2.issuperset(set1))
# print(set1.issubset(set2))
# print(set2.intersection(set1,set3))
# print(set2.difference(set1))
# print(set1)
# print(set1.remove(1))
# print(set1)
# print(set1.add(4))
# print(set1)
#
# fs = frozenset ({1, 2, 3})
# print(fs)
#
# fs.add(4)
# print(fs)

# fs = set({1, 2, 3})
# print(fs)


# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# list_1= ['Hi', 'ananas', 2, None, 75, 'pizza', 36, True, 100]
#
# result = (filter (lambda x : isinstance(x, int),list_1))
# print(result)
# print(sum(result))

# sum=0
# for i in list_1:
#     if type(i) == int or type(i) == float:
#         sum += i
# print(sum)

# print('original list : ', list_1)
# print('sum of all numbers: ', sum([x for x in list_1 if type(x) == int]))


# list_1= ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# tuple1 = tuple(list_1)
# result = tuple(filter(lambda x: isinstance(x, str), tuple1))
# print(result)

# 3.3
# list_1= ['cat', 'dog', 'horse', 'cow']
# tuple1 = tuple(list_1)
# print(tuple1)

# 3.4
# my_family1 = input('введіть імена сімі1:\n')
# my_family_list1 = list(my_family1)
# new_my_family_list1 = my_family1.split(' ')
# my_family2 = input('введіть імена сімі2: ')
# my_family_list2 = list(my_family2)
# new_my_family_list2 = my_family2.split(' ')
#
# print(new_my_family_list1)
# print(new_my_family_list2)
#
# result_1 = [print(i, end=", ") for i in new_my_family_list1]
# print(result_1[-1])

# my_family1 = input('введіть імена сімі1:\n').split(', ')
# my_family2 = input('введіть імена сімі2:\n').split(', ')



# a = len(new_my_family_list1)
# b = len(new_my_family_list2)
# if a>b:
#     print(new_my_family_list1)
# elif a<b:
#     print (new_my_family_list2)
# elif a==b:
#     print ('equal')


# 3.5
# Film = {
#      'title':'1+1',
#      'director': 'Оливье Накаш',
#      'year': '2011',
#      'budget': '$ 11 500 000',
#      'main_actor': 'Франсуа Клюзе',
#      'slogan': 'Неприкасаемые'
#
# }
# print(Film.keys())
# print(Film.values())
# print(Film.items())

# 3.6

# my_dictionary = {
#     'num1': '375',
#     'num2': '567',
#     'num3': '-37',
#     'num4': '21'
# }
# print(my_dictionary.values())
#
# new_list = list(my_dictionary.values())
# print (new_list)
# print (type(new_list))
#
# result = [int(item) for item in new_list]
# print(result)
# print(sum(result))

# print(sum(my_dictionary.values()))
# 3.7

# list3 = [1, 2, 3, 4, 5, 3, 2, 1]
# list_3 =list(set(list3))
# print(list_3)

# 3.8

# set1 = {'a','z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, '1', 785}
#
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.issuperset(set1))


# list_1 = [1, 6, 4, 7, 9, 1, 2, 7]
# print(list_1)
# print(id(list_1))
# list_1.sort()
# print(list_1)
# print(id(list_1))
# print(sorted(list_1))
# print(id(sorted(list_1)))
#
# new = [x*x for x in list_1 if x%2 == 0]
# print(new)
#
# for x in list_1:
#     if x%2 ==0 ;
#     new_2.append (x*x)
#     print (new_2)

# tuple_0 =('mark',)
# tuple_1 = ('mark', 26, ['214 Rua Trindade Coelho','Parede', 2779-293])
# list_3 = list(tuple_1)
# print(list_3)
# list_3{}


# list_1 = [1, 6, 4, 7, 9, 1, 2, 7]
# print(list_1)
#  list_1 = list(set(list_1)) #убиарем дупликаты
# print(list_1)

# dict_1 = {} #create dict from list
# for ind in range(len(list_1)):
#     print(ind)
#     dict_1[ind] = list_1[ind]
# print(dict_1)
# print(*dict_1) #распаковка- печатает только данные
# print(dict_1.keys())
# print(dict_1.values())
# print(dict_1.items())
#
# for ind, val in enumerate (dict_1.values()):#раскрываем индекс +значение
#     print(f'{ind}-{val}')

# # если работодатель чекает тое время за компом - что б показать что акт польз компом запусти

# import pyautogui
# import time
# while True:
#     pyautogui.press('Tab')
# time.sleep (10.0)
#
# def person( name, last_name, age):
#     return f'Hello my name is {name} {last_name}. i am {age} years old'
# print(person('anna', 'smith', 35))


# x = 15
# y = 78

# def sum_it(x,y):
#     print(f'locals: {locals()}')
#     return x+y
#
# print(f'Inside the function: {sum_it(5,8)}')
# print(f'Outside the function: {x+y}')
# print(f'Globals: {globals()}')

# # lambda functions
# print((lambda x, y: x*y)(5,8))
# mult = lambda x, y: x*y
# print(mult)
#
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# def filter_and_sum_nums(l):
#     new_l = []
#     for i in l:
#         if i in l:
#             if isinstance(i, int):
#                 new_l.append(i)
#     return sum(new_l)
#
# print(filter_and_sum_nums(list_1))

# print(sum(filter(lambda x: isinstance(x, int), list_1)))


# print (____filter add_nums with custom function___)

# def take_odd(num):
#     if isinstance(num, int) and num%2:
#         return True
#     return False

# print(list(filter(take_odd, list_1)))
#
# list_3 = [1, 2, 5, 8, 10, 105, 78]
# print(list(filter(take_odd, list_3)))

# print(-----filter odd_nums and lambda___)
# filtered = list(filter(lambda x:isinstance(x, int), list_1))
# print(list(filter(lambda x: x%2, filtered)))

# print(list(filter(lambda x: x%2, list_3)))

# print(---- filter strings with "a" using custom function----)
# new_l = []
# for item in list_1:
#     if isinstance(item, str) and "a" in item:
#         new_l.append(item)
# print(new_l)

# # print (FILTER STRING WITH USING LAMBDA)
# filtered = list(filter(lambda x:isinstance(x,str), list_1))
# print(list(filter(lambda x: 'a' in x, filtered)))

# MODULES
# import functools
# res = functools.reduce(lambda x,y: x+y, [1, 5, 8, 11, 13])

# from functools import reduce
# res = reduce(lambda x,y: x+y, [1, 5, 8, 11, 13])
# print(res)
#
# import my_file
# res = my_file.sum_it(5,8)
# print(res)

# from my_file import sum_it,prod
# res = sum_it(5,8)
# print(res)
#
# res1 = prod(5,8)
# print(res1)

# from my_file import *
# res = sum_it(5,8)
# print(res)
#
# res1 = prod(5,8)
# print(res1)
#
# from my_file import *
# def tests():
#       assert sum_it(5, 8) == 13, f'wrong number, actual resul {sum_it(5,8)}'
#       assert prod(10, 6) == 60, f'wrong number, actual result {prod(10,6)}'
#       # assert div(10,0) == 'can not divide by zero'
# tests()

#  встроеные модули

import math

from math import *

# arr = [1, 2, 3, 4, 5, 10, 25]
# new_arr = math.prod(arr)
# print(new_arr)

# allias
# import math as m
#
# arr = [1, 2, 3, 4, 5, 10, 25]
# new_arr = m.prod(arr)
# print(new_arr)

# import datetime
# birth_year = 1980
# current_date = datetime.date.today()
# current_age = datetime.date.today().year - birth_year
# current_month = datetime.date.today().month
# print(current_date)
# print(current_age)
# print(current_month)

# def sum_it(**kwargs):
#     result = 0
#     for i in kwargs.values():
#         result += i
#     return result
#
# print(sum_it(num1=4, num2=5, num3=10))

# def sum_i(*args):
#       return sum(args)
# print(sum_i(5, 6, 10))


#  функция периметра / диагонали квадрата
# def square(x):
#     perimetr = x*4
#     square = x**2
#     diagonal = x**(1/2)
#     return perimetr, square, diagonal
#
#
# print(square(5))



# def about(name, last_name, age):
#     return f' name:{name},\n last name: {last_name},\n age: {age}\n'
#
# print (about('alona', 'kuts',32))

# def name_arg(**kwargs):
#     for key, value in kwargs.items():
#         print('{}:{}'.format(key,value))
# name_arg(name='alona', last_name='kuts')

# 4.2
# def about1(name = 'alona', last_name = 'kuts', age = 35, position = '-'):
#     return f' name: {name},\n last name: {last_name},\n age: {age}, \n position: {position}'
#
# print (about1('andrii', 'kuts', 36))

# 4.3
my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x>=0, my_list)))

# # 4.4
# from functools import reduce
# print(reduce(lambda x, y: x * y, my_list))

# 4.5
# from my_calc import *
# res = sum_it(5, 8)
# print(f'сумма чисел: {res}')
#
# res_1 = minus(8, 8)
# print(res_1)
# #
# res_2 = mnozh(5, 9)
# print(res_2)
#
# res_3= dil(5, 0)
# print(res_3)



# from my_calc import *
# def tests():
#       assert sum_it(5, 8) == 13, f'wrong number, actual resul {sum_it(5,8)}'
#       assert minus(5, 8) == 3, f'wrong number, actual result {minus(5,8)}'
#       # assert div(10,0) == 'can not divide by zero'
# tests()





























