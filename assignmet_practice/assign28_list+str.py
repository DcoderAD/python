# remove all non int values for the list
# l=[12,'a',2.3,4+9j,True,90]
# l1=[]
# for e in l:
#     if type(e)==int:
#         l1.append(e)
# print(l1)
                    # or
# plsease chk output it was giving error earlier
# l=[12,'a',2.3,4+9j,True]
# i=0
# l1=[]
# while(i<len(l)):
#     if type(l[i])==int:
#         l1.append(l1[i])
#     i+=1
# print(l1)    




# print distinct elements and their frequencies in a list
# l1=[1,2,3,3,4,5,5,1,1,8,9,0,1,0,3,7]
# i=0 
# for x in l1:
#     if i==l1.index(x):
#         print(x," ",l1.count(x))
#     i+=1



# sort a list of strings
# s=['bhopal','jaipur','udaipur','indore','ajmer']
# s.sort()
# print(s)



# find the first repeated string in the list of strings
# l1=['ab','bc','bc','ab','bc','cb']
# i=0
# for s in l1:
#     if l1.index(s)!=i:
#         print("first repeated string is",s)
#         break
#     i+=1



# count strings which ends with 's'in the list of strings  
# l=['bhopal','jaipur','udaipur','indore','ajmer','delhi','mumbai','pune']
# count=0
# l1=[]
# for e in l:
#     if e.endswith('i'):
#         l1.append(e)
# print(l1)


