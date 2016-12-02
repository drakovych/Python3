
def func1(one):
    one = one * 3
    def func2(two):
        return two + one
    return func2

func = func1(2)
y = func(10)
print(func)
print(y)
