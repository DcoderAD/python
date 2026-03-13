# create list of first n even natural numbers
# n=int(input("Enter number"))
# # print([2*i for i in range(1,n+1,1)])

                        # or
#   


# first n term of febonnacii series
# n=int(input())
# a,b=-1,1
# l=[]
# while n:
#     c=a+b
#     l.append(c)
#     a,b=b,c
#     n-=1
# print(l)





#create a list of first n prime numbers

# n=int(input("enter number"))
# l3=[]
# x=2
# while n:
#     for e in range(2,x):
#           if x%e==0:
#                break
#     else:
#         l3.append(x)
#         n-=1
#     x+=1
# print(l3)



#add two matrics each of order 3X3.store matrix in a list
print("Enetr 9 elements of matrix.give comma after each 3 elements")
l1=[
    [int(i) for i in input().split(',')],
    [int(i) for i in input().split(',')],
    [int(i) for i in input().split(',')]
  ]

print("Enter 9 elements of matrix (row wise) seprated by comma")
l2=[
    [int(i) for i in input().split(',')],
    [int(i) for i in input().split(',')],
    [int(i) for i in input().split(',')]
   ]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        c[i][j]=l1[i][j]+l2[i][j]
        print(c[i][j],end=" ")
    print()
print()



# create 2 lists from given list one of them contain positive elements and other one nagetive element
# l=[1,-1,2,-2,3,-3,4,-4]
# p=[]
# np=[]
# for e in l:
#     if e<0:
#         np.append(e)
#     else:
#         p.append(e)
# print(p,np)

