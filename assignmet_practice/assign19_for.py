#print correusponding Unicode of each character of string
# a=input("Enter string")
# for i in a:
#     print(ord(i),end='')


# print only vowels in the given strint
# a=input("Enter your string")
# for i in a:
#     if i!='aeiou' or'AEIOU':
#         continue
#     else:
#         print(i)

#COUNT SPACES IN THE STRING
# count=0
# a=input("ENter string")
# for e in a:
#     if e==' ':
#         count+=1
# print(count)

# print unique digits of a givn integer means no repeatition?
n=int(input("Enter number"))
k=''
for e in str(n):
    if e in k:
      pass
    else:
       print(e)
    k+=e

# unique digit using index() function because index function always give unique single index number for unique element is does not give another index to same element
s=input("Enter string")
i=0
for e in s:
   if s.index(e)==i:
      print(e,end=' ')
   i+=1
    


# count number of digits in given integer
# a=int(input("Enter number"))
# count=0
# for e in str(a):
#     count+=1
# print(count)