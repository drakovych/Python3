ListInList = [1, [2, 3], 4, [[6, 7]]]
new_ListInList = []


def flatten(x):
    new_ListInList = []
    for item in x:
        if type(item) == list:
            for item_1 in flatten(item):
                new_ListInList.append(item_1)
        else:
            new_ListInList.append(item)
    return new_ListInList


print(ListInList)
print(flatten(ListInList))
input()
