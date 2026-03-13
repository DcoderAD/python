#calculate sum of elements of list
# sum=0
# l=[1,2,3,4,5]
# for e in l:
#     sum=sum+e
# print(sum)

                    # or

# print("Enter elements")
# l=[int(e) for e in input().split(',')]
# print(sum(l))






#average of elemet of list
# sum=0
# count=0
# l=[1,2,3,4,5]
# for e in l:
#     sum=sum+e
#     count+=1
# avg=sum/count
# print(avg)

                        # or
# print("Enter values saperated by comma")
# l=[int(e) for e in input().split(',')]
# avg=sum(l)/len(l)
# print(avg)





#square of element of given list
# l=[1,2,3,4,5]
# print([e**2 for e in l],end=' ')
                    # or
# best and short way
# print("Enter value saperated by comma") 
# print([(int(e))**2 for e in input().split(',')])
                    #or
# print("Enter value saperated by comma") 
# l=[(int(e))**2 for e in input().split(',')]
# l2=[e**2 for e in l]
# print(l2)





# sort list elements in decending order
# print("Enter value sep by comma")
# l=[int(e) for e in input().split(',')]
# l.sort() #ascending order print
# print(l)
# l.sort(reverse=True) #descending order print
# print(l)
 
 
 
 
 # create list from a givrn list selecting only even place elements
# print("Enter number sep by comma")
# l=[int(e) for e in input().split(',')]
# i=1
# l2=[]
# for e in l:
#     if i%2==0:
#         l2.append(e)
#     i+=1
# print(l2)