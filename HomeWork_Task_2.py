"""Please don't user builtins for naming
   'str', 'list', 'dict', 'set' etc. deprecated.
   Always and your code files with new line.
"""
str = '((((((((((((((2, 3)))))))))))))'
left_sk = str.count('(')
right_sk = str.count(')')
print ('Left bracket', left_sk)
print ('Right bracket', right_sk, '\n')
str_new = str + ')'
print ('Old string', str)
print ('New string', str_new)
input()
