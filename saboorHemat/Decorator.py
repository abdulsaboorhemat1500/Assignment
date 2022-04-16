def inc(x):
    return x+1
def dec(x):
    return x-1

def oper(fun,x):
    result=fun(x)
    print(result)


print("incremented")
oper(inc,10)
print("decremented")
oper(dec,10)