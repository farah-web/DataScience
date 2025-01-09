# -*- coding: utf-8 -*-
import copy
a = [[1, 2], [3, 4]]
#b=a.copy()
b=copy.deepcopy(a)
print("b is : ",b)

print(id(a[0][0]))
print(id(b[0][0]))
b[0][0]=333
print(b[0][0])
print("changed value in a ",a[0][0])
