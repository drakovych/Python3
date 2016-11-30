def func1(x):
    def func2(y):
        return x + ' it\'s ' + y
    return func2


func = func1('foo')
x = func('bar')
print(x)
