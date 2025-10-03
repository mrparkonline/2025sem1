# FUN STUFF
def fun(x):
    if x in {0,1}:
        return x
    else:
        return fun(x-2) + fun(x-1)
print(fun(40))