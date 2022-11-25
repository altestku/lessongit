def sum_it(x, y):
    return x+y

def minus(x, y):
    return x-y

def mnozh(x,y):
    return x*y

def dil(x, y):
    try:
    # assert y !=0, 'на ноль делить нельзя'
        return x/y
    except:
        return 'на ноль делить нельзя'
