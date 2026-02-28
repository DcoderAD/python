"""String"""
"""
(1)str is a class
(2)str is a sequence
(3)str is is iterable
(4)str elements are indexed.+ve and -ve both
(5)str is immutable(same sa range).no changes once created

"""

"""How to create str object"""
# s1='ajay'
# s2="ajay"
# s3="""ajay"""
# s4='''ajay'''
# s5=str() #empty str object.
# s6=str('ajay')#also create object 
# s7=str(1234) #str fun. conversion function ki tarah bhi kam karta hai.1234 converted to string '1234'.
# s8=str(3+4j)#complex number bhi str me convert ho jayega
# s9=str(4.5)#convert into str
# # print(s9,type(s9))
# s10=str([2,4,10])# print a single string.not individual elements
# # print(s10)



"""indexing concept in str"""
# s1='ajay'
# print(s1[0])# print first char 'a' 
# print(s1[-1])#last char print


"""accessing str value: 4 methods
    FIRST SIMPLE PRINT
    SECOND USING FOR LOOP
    THIRS USING WHILE LOOP
    SLICING OPERATOR
"""
# s1='ajay education services'
# print(s1)
                  # or 


#print using for loop
# for e in s1:            
#     print(e,end='')
# print()

 
                 # or


#print using while 
# s1='ajay education services'
# i=0
# while i<len(s1):         loop
#     print(s1[i],end='')
#     i+=1
# print()

                #or


 #print using slicing               
# s1='ajay education services'  
# print(s1[::])               
# print(s1[2:10:3])       #will count space too
# print(s1[::-1])         #reverse the string



"""built in method : apply to all iterables"""
# #we pass iterable as an argument in builtin method
# s1='ajay education services'
# print(len(s1)) #strig length
# print(max(s1)) #max unicode value alphabate
# print(min(s1)) #min unicode value alphabate(here it gave "space" jiska unicode smallest hai)
# # print(sum(s1)) #error
# print(sorted(s1))#sort data accorfing to unicode size.and it returns  list of sorted elements

"""concatination and repetition operator"""

# concatination
# s1='ajay'
# s2='edu'
# s3='services'st
# s4=s1+' '+s2+' '+s3 #concatinate all three strings
# print(s4)

# # repeatition operator
# print(s1*3)#repeat krega 3 bar