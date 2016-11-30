
def func(first):
    foo = first * 2
    def func2(second):
        # nonlocal foo
        return second * 10
    return func2
    def func3(third):
        return foo // 3
    return func3


x = func('foo')
y = x(10)
# z = x.func.func3(100)

print(x)

print(y)
