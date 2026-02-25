# LIST PART-2

"""Packing and unpacking"""

# UNPACKING
# l1=[25,56,71] #its pack like single unit.how to unpack it?
# a,b,c=l1  #l1 me 3 value hai to var. bhi 3 banenge nahi to error.
# print(a,b,c)#


#PACKING
# l1=[25,56,71]
# a,b,c=l1
# l2=[b-1,a+2,c+5]#a,b,c ko kisi bhi sequence me rkh skte hai
# print(l2)



# #BUILT IN METHOD-USEFUL FUNCTIONS OF PYTHON
# len()
# max()
# min()
# sum()
# sorted()
# ye kisi class ke member function nahi hai just simple non member functions hai.so we dont call them by object.function()
# ye 5 fuctions iterables pe apply hote hai REMEMBER

# len()
# l1=[25,56,71]
# print(len(l1))


# max() biggest element
# l1=[25,56,71]
# print(max(l1))

# min()
# l1=[25,56,71]
# print(min(l1))

# sum()#
# print(sum(l1))


# sorted() function list in indexing ko actuall me change nahi karta hai.sorted function list ke elements ko le kr,sort kr, new list bna kr deta hai.
# sorted function() always returns list and argument me di gayi list me koi changes nahi krta hai
# l2=[54,1,20]
# print(sorted(l2))--->[1,20,54]
# print(l2)----->[54,1,20]


# l4=[12,3.4,5+8j]
# print(max(l4))# error.comparision hoga jo ki int and compex me > nahi kr payega


# Object kese banaye list ka?
# l1=list() #empty list 
# l2=list(10,20,30)#error.list methoooood me 1 se jyada argument pass nahi kar skte.
# l2=list(10)#error.list me diya hua argument must be an iterable.10 to int he 


# l2=list(range(4))#ye sahi hai.list me iterable pass ho raha hai
# print(l2) #---->[0,1,2,3]


# l2=list(range(4))------>list bhi conversion function ki tarah kam kar pa raha hai jese int(input) me str se int me conversion hota hai.wese hi range ke 4 element list type ke element ban jayenge


# l3=list("education") 
# print(l3)
#---->yaha str bhi iterable hai to is string ka each element...l3 list ke 9 element ban jayenge.


# comparing list elements
# l1=[1,2,3]
# l2=[2,1,3]
# l3=[1,2,3]
# print(l1==l2)#false .kyuki elements ka order same nahi hai
# print(l1==l3)#true  .same element same index pe hai
# print(l1>l2) #false #dono ke first element compare honge jo bada hoga wahi list bhi badi hogi.agar first element sam hota to second elements compare hote



# concatination operator

# l1=[1,2,3]
# l2=[2,1,3]
# print(l1+l2)#---->[1,2,3,2,1,3]

# # repetition operator
# print(l1*3)#---->[1,2,3,1,2,3,1,2,3] 