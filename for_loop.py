# for i in "ajay":
#     """4 bar loop chalega ek ek alphabate ko cover krne ke liye"""
#     print(i)


#write script to count 'a' in given string 
# a=input("Enter a string")
# count=0
# for i in a:
#     if i=='a':
#          count+=1
# print(count)


#when to use while loop??
#jab kisi condition ke true rhne tak repeation chahiye & condition false hone pe repeation ruk jaye tab use kare while loop

"""when to use for loop???
as we know for loop iterables pe lagta hai.so iterable type ka jo bhi object hum banayenge.for code ko utni bar chalayega jitne elements iterable me hai.so for loop ispe based hai ki iterable me kitne elements hai unki counting based hai
"""

#break,pass,continue ka use hota hai yaha for loop me bhi


# use break when c comes in string and till then print capital latters 
# for e in "abbabbaaabbbbcabgggc":
#     if e=='c':
#         break
#     print(chr(ord(e)-32),end='',)

#use of continue to skip the c character    
# for e in "abbabbaaabbbbcabgggc":
#     if e=='c':
#         continue
#     print(chr(ord(e)-32),end='')


#we can use else with foe loop too
"""print all character from the given string,but stop printing if r appeare in the sequence.if all character printed successfull then print
all element are printed
"""
# for e in input("Enter a string"):
#     if e=='r':
#         break
#     print(e,end=' ')
# else:
#     print("all element are printed")
# print("terminated using break")



#same code for ki dont print the r baki sab print kro
# for e in input("Enter a string"):
#     if e=='r':
#         continue
#     print(e,end=' ')
# else:
#     print("all element are printed")
# print("terminated using break")