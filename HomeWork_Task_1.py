"""It isn't valid realization. This must work authomaticaly.
   When I send to to your program 'list' instance via argv
   or via input/raw_input the output must be flaten list.
   [1, 3, 5, [6, 10, 3, [2, 3], 3], 8]
   ==>
   [1, 3, 5, 6, 10, 3, 2, 3, 3, 8]
"""
lst = [1, [2, 3], 4, [[6, 7]]]
lst_new = lst[0:1] + lst[1][0:1] + lst[1][1:2] + lst[2:3] + lst[3][0][0:1] + lst[3][0][:2]
print (lst)
print (lst_new)
input()
