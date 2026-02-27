# # how do we handle string in eval() ??

# x=eval(input("Enter your data"))
# match x:
#     case x if type(x)==int:
#         print("monday")
#     case x if type(x)==float :
#         print("tuesday")
#     case x if type(x)==complex :
#         print("wednesday")
#     case x if type(x)==bool :
#         print("thursday")
#     case x if type(x)==str:
#         print("str with eval how to handle it?")
#     case _:
#         print("None")


# print unique digits of a givn integer.
# fir se try kiya kal wala logic sabhi cases me shi answere nahi de raha tha plz check this one sir


# s=''
# for e in str(int(input("Enter number"))):
#     if e in s:
#       pass
#     else:
#        print(e,end=', ')
#     s+=e


# l2=list(range(4))------>list bhi conversion function ki tarah kam kar pa raha hai jese int(input) me str se int me conversion hota hai.wese hi range ke 4 element list type ke element ban jayenge



count digit in a given number
count=0
for a in str(int(input("enter a number"))):
    if a is not None:
        count+=1
print(count)




# calculate sum of given numbers
# bar bar  type conversion manipulation thik hai?
# pah;e num ko str me convert kr ke input liya kyuki for loop me iteration krna tha then if sum ka kahi use krna ho to e ko agai int bana ke joda
# sum=0

# for e in str(input("Enter your number")):
#     sum=sum+int(e)
# print(sum)


#list me element number same honi zaruri he?
l4=[[32,22,4],[54,55,62],[7,12,43]]
for i in range(0,3,1):
    for j in range(0,3,1):
        print(l4[i][j],end=' ')
    print()



l1=[23,34,45,56,67]
print(l1)
l1.append(33)
print(l1)# give correct putput
print(l1.append(84)) #give None why??
