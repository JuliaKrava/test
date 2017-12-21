
def func(*arg):
    a=list(arg)
    a.sort()
    return a[1]
print(func(10,2,5,7,5,988,7,12))