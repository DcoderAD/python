# list
"""
its a class in python

list is iterable 

list is a sequence

list support indexing both +ve and -ve like range
"""

# range vs list
"""
range me object create hone ke bad change(Edit,Grow,Reduce any change) nai kar satkte hai..this is why range is immutable.

list is mutable type we can edit,delete,add,insert element. list is growable

range can contain only integer data.But in list you can store element of any type

""" 
# how we create list object
# l1=[10,20,30]
# l2=[4.5,True,'abc',34,3-6j]#hetrogeneous list
# l2=[]#this is empty list it will print []
# print(l1,l2,end='\n')#range ko for loop se hi print krwa pa rhe the


# how to access list elements
# print(l1)       #direct print [10,20,30] as it is
# l1=[10,20,30]
# print list element using for loop
# for e in l1:
#     print(e,end=' ')#print without [ ].only 
                        # print elements

# print using while loop.use for loop wo better hai
"""
l1=[10,20,30]
i=0
while i<=2:
    print(l1[i],end=' ')
    i+=1
print()
"""
# print using individual indexing
"""
l1=[10,20,30]
print(l1[0],l1[1],l1[2])
"""
#negative 
"""
l1=[10,20,30]
print(l1[-1])
"""

#delete element using del keyword
# l1=[10,20,30]
# print(l1)
# del(l1[0])
# print(l1)

"""
list internally kese work kr raha hai??
list l1 ek list object ko refere kr raha hai.jinme each index pe variables hai.or ye variable int objects ko refere kar rahe hai. 0,1,2 index pe rakhe variable  10,20,30 int object ko refere kr rhe hai.jab aap del(l1[0]) krge to index 0 wala 10 remove ho jayega and 20 and 30 ki indexing 0,1 ho jayegi

actually internally ye list hai references ki jo int objects ko refere kar rahi hai.

"""


# how do we edit element of a list??
# print(l1)   #[10,20,30]
# l1[0]=77
# print([l1]) #[77,20,30]

#invalid index will give always give error
#kya hoga out of list element print try lrenge to
# l1=[10,20,30]
# print(l1[5]) #index out of range error

# edit an element
# l1=[10,20,30]
# l1[2]=50 #[2] pe pahle se 30 tha wo replace ho jayega with 50
# l1[3]=300 #ye error dega kyuki l1[3] index to hai hi nahi .so element add krne ka differet method hai
# print(l1)

"""how to add new element to the list(iske bhi 2 tarike hai)"""

# as we know class is a group of variable and functions
# 2 functions in list class---> append()   ,   insert()

# append()---->list me last me last me ek value jod dega

# ye functions append(),insert() ya method only list class ke hai to usi class ke object  se call honge.means list methods can only be called via list bject

# listObject.listMethod()

# l1=[10,20,30]
# l1.append(25)
# print(l1)


# insert()------>ye function elements ke bich me bhi insert kar sakta hai element ko
# so insert(index,element) me do value deni hoti hai ek to kis index pe insert krna hai and konsa element insert karn hai

# agar l1[0] pe element insert karoge to pahle se available index 0 wala element aage shift ho jayega and baki ke elements bhi sabhi shift ho jayenge.
# ye elements ko replace nahi krta hai shift kar deta hai 
# list me index 0,1,2 hi hai but insert() function me 3,4,5..... de kr element insert karwane pe error nahi dega ...na hi indexing ka gape create karega...last idex ke just baad me us element ko append kr dega

# l1=[10,20,30]
# l1.insert(0,333)
# print(l1)
# l1.insert(7,900) #wont give error it will append in last
# print(l1)
