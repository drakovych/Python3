str = '((((((((((((((2, 3))))))))))))))'


def brackets(old_string):
    y = -1
    for item in old_string:
        if item == '(':
            #            x += 1
            while old_string[y] != ')':
                print(old_string[y])
                y -= 1
                print(y)
                if old_string[y] == '(':
                    print('Close brackets \')\' !')
                    break
            else:
                y -= 1
                print('All ok!')


brackets(str)
input()
