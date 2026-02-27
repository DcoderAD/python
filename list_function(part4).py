"""list Class Methods/Functions"""
# jab list class ka pbject banate hai to us class ke functions ko "object.function()" se call karte hai

# append(),insert() dekh chuke hai  

# append
# count()  index()  remove() pop() clear() reverse() sort()


l1=[23,34,45,56,67]
print(l1)
l1.append(34)
print(l1)#will give right answere
print(l1.append(84)) #none answere dega


l1.insert(2,122)
print(l1)

print(l1.count(10))# ans=0 kyuki no 10 in l1
print(l1.count(122))# 1 bar 122 aa raha hai

print(l1.index(122))#will return index of 122
# agar 122 1 se jyada bar aayega to left se jo phle index wala 122 hoga wo index dega

print(l1.index(122))#error dega

# remove() function list ka function hai baki delete del se bhi hota hai
l1.remove(122)#122 delete ho jayegi
print(l1)
# l1.remove(133)#will give error 133 list item nahi hai


# pop
a=l1.pop()#last index wala element delete hoga
print(a)
print(l1)


# reverse
l1.reverse()#reverse element
print(l1)

# sort->ye list class ka function hai.ye list me directly change kr deta hai
# sorted-> ek builtin method pada tha usme jo iterable pass lrte the wo use sort kar ke new list bna ke deta tha original list me koi change nahi krega
l1.sort()
print(l1)

# clear
l1.clear() #clear the list
print(l1)