from itertools import chain
listmerge = lambda *lst: list(chain(*lst)) 
y = listmerge(*[[1,2], [3,4], [5,6,7], [8]])
print(y)