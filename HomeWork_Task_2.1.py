str = '((((((((((((((2, 3)))))))))))))'


def brackets(old_string):
    x = 0
    y = 0
    for item in old_string:
        if item == '(':
            x += 1
    for item in old_string:
        if item == ')':
            y += 1
    if x > y:
        print(x, y)
        print('не хватает скобки )')
    if x < y:
        print(x, y)
        print('не хватает скобки (')


brackets(str)
input()
