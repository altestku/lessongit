arr1 = [1, 2, 4]
arr2 = [3, 5, 7, 8]



def calc(*args):
    result = 0
    for i in args:
        if isinstance( i, list):
            for k in i:
                result += k
        else:
            result += i
    return result


res1 = calc(arr1, arr2, 3)
    # print(args[0])
# calc(arr1, arr2)
print(res1)

