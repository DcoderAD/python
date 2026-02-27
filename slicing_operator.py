# Slicing-operator(range type ka hai but difference hai)
"""
listObject[beg:end:step] yaha : hai range me , tha
beg==>starting index(always inclusive)
end==>end index(always exclusive)
step==>increment or decrement amount
"""

l1=[34,45,65,77,1,2,22,98,87 ]
print(l1[1:6:2])   #will return a sub list  


# no begining value given then. 
# print(l1[:6:2])? 
#  when step is positive begin is by default index 0.0index se start hoga
#if no beg+negative index to extreme right se pring hoaga means index -1
print(l1[:6:2])
print(l1[:6:-1])


print(l1[::])#it will print complete list
print(l1[::-1])#print list element in reverse
#end nahi diya hai to ye extreme end ko bhi include kar lega exclude nahi karega remember
#byDefault step=1
#byDefault beg=0
#byDefault end=extremen end