lst = [1, [2, 3], 4, [[6, 7]]]
lst_new = lst[0:1] + lst[1][0:1] + lst[1][1:2] + \
    lst[2:3] + lst[3][0][0:1] + lst[3][0][:2]
print(lst)
print(lst_new)
input()
