#first n even natural number
# r= range(1,int(input())+1)
# for e in r:
#     print(e*2)




# FIRST N ODD NATURAL NUMBERS
# r= range(1,int(input())+1)
# for e in r:
#     print(e*2-1)



#SQURE OF FIRST N NATURAL NUMBERS
# r= range(1,int(input())+1)
# for e in r:
#     print(e**2)



# CUBE OF FIRST N NATURAL NUMBERS
# r= range(1,int(input())+1)
# for e in r:
#     print(e**3)


# DISPLAY ALL PRIME NUMBERS WITHIN range
# START=15,END=45
prime=[]
for num in range(15,48,1):
   if num>1:
      for a in range(2,int(num**0.5)+1):
            if num%a==0:
                break
            else:
                prime.append(num)
print(prime)