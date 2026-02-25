"""
range is data type and all data type in python are classes


its a iterable  


range is sequence...means its in lenier arrangement.its like position or indexing system


range elements are indexed
not all iterables are in sequence
for example set,dict


LIMITATION-->range objects can contain only int type values.

IMPORTANT-->range contains a sequence  of integer with common difference(Arithmatic progression)
exp. 1--4--7--10--13--same difference of 3    
"""

#how we make object of range?
# range() likhne se range object ban jayega fir ise var.me assign kr de.
# r1=range()


# jese x=int(5) se int class ka object banta hai wese hi x=range() se range class ka object banega


# har data type ke aage () lagane se wo conversion function ban jata hai.jese range() se ye ek function ban gaya hai.is function ke call hone se range ka object bana.jiska id return hoga and r1 me chala jayega


# r1 me kya jayega?
# r1=range(beginning,end,step)
# beginning==>first element or startin value
# # step==>common difference
# end==>just greater value then the last element.kyuki end value always exclude hogi.

#1,4,7,10,13,16 diya hai to 
# beg=1
# end=17(end 22 na le nahi to range me last 19 aa jayega just end se 1 num.jyada lele )
# step=3



# r1=range(1,17,3)
# print(r1) 
# will print range(1,17,3) not the elements
# to print the elements use for loop bcz for loop works with iterables

# print this 1,4,7,10,13,16
# r1=range(1,17,3)
# for e in r1:
#     print(e,end=' ')


# print 10,20,30,40,50,60 using range
# r=range(10,61,10)
# for e in r:
#     print(e,end=' ')


#print 100,95,90,85,80,75
# r=range(100,74,-5)
# for e in r:
#     print(e)






#r1=range(beg,end,step)
#r2=range(beg,end) | step=1 mana jayega by default
# r=range(10,20)
# for e in r:
#     print(e,end=' ')



# if r=range(end), ek hi value dene par wo end consider hoga and beginning=0 and step=1 mana jayega
# r=range(5)
# for e in r: 
#     print(e)



# # how do we access a perticular element in the range??
# we will use indexing.range me -ve indexing bhi hoti hai.python me har sequencing wale iterator me indexing milegi.sequence me hamesha integer aayenge float char kabhi nahi aayenge remember this
# range me position 0 se start hogi
#  0 1 2 3 4  5  6  7  8  <----index
 # 2,4,6,8,10,12,14,16,18(index ya position reserve hai change nahi hogi...and position hamesha 0 se start hogi)
# r=range(2,20,2)
# print(r[5])#--->12

# r=range(2,20,2)
# print(r[-1])



#first 10 natutral number using range and for loop
# r= range(1,11,1)
# for e in r:
#     print(e)

#square of first 10 natural number using range and for loop
# r= range(1,11,1)#steo 1 hai to na bhi likhe to chlega
# for e in r:
#     print(e**2)

#first n even natural number in reverse order
# n=int(input("enter n \n"))
# r=range(2*n,1,-2)
# for e in r:
#     print(e)

    # or


# n=int(input("enter n \n"))
# r=range(n,0,-1)
# for e in r:
#     print(2*e)


    # or

# r=range(int(input("enter n \n")),0,-1)
# for e in r:
#     print(2*e)