#either code will run and print 1 to 10 or if user enter 25 loop ends
# i=1
# while i<=10:
#     print(i)
#     x=int(input("Enter a number"))
#     if x==25:
#         print("25 is break number so program ends here")
#         break
#     i=i+1


# use of continue.....below written code will run for ever
# i=1
# while i<=10:
#     print(i)
#     continue# wrong place to use continue
#     i=i+1 #continue i ko increment hi nhi hone dega



"""ske use ka classic example hai ki ek esa program jisme 10 number input krega user but wo even hua to print hoga nahi to skip ho jayega """
i=1
while i<=10:
    x=int(input("enter a number"))  
    if x%2==0:
        continue #10 number print honge but even ko ye skip krwa dega.ye continue 1 ki value change hone hi nahi de raha hai agar odd enter kiya to.so ye 10 odd number le kr hi finish hoga 
    print(i,x)
    i+=1