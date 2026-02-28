"""tuple"""
#list and tuple ka comparision bhi hota hai.some differences are there thats it
#array(in c/c++) vs list(python)--->array fix size ka banaya jata hai ....but list growable hoti hai.list me different tpe of value rakh skte hai normally array me similar type value hi aati hai

# tuple is a class
# tuple is iterable
# tuple is a sequence #jo bhi sequence honge indexing hogi hi
# indexing is there.+ve and -ve 
# tuple is immutable.list is mutable this is the biggest difference btw both
# tuple can contain values of different types
# tuple me slicing operator work krta hai
# list comprehension ki tarah tuplecomprehension nahi hota hai



#                     #tuple object creation
# t1=(11,22,33,44) #paranthisis me likhe elements are tuple
# print(t1,type(t1))



# t2=(11,2.3,'a',4+4j,True)
# print(t2)


# t3=()
# print(t3,type(t3))

# #single value wala touple nahi hoga ye int hai REMEMBER
# #( ) me single value dene se ye touple nahi baneha this is exception
# #list me 1 value de sakte hai 
# t4=(10)#int class object
# print(t4,type(t4))

# t4=(10,) #(10,) comma lagane se ye touple object ban jayega.single element ke sath touple element banane ka ye sahi tarika hai comma use kr ke bana skte hai
# print(t4,type(t4))#touple class object


# t5=10,20,30,40,50,60 #no () fir bhi ye touple type hai
# print(t5,type(t5))

#                 #element access using indexing
# print(t5[4])

# # print(t4[45])#out of range index error dega

# print(t5[-1])#last indexed element return

#buitlin method bhi work krte hai touple me
# accessing elements using loops
# t5=10,20,30,40,50,60
# i=0
# while(i<len(t5)):
#     print(t5[i])
#     i+=1
# print()


# for i in t5:  #use for loop its better
#     print(i,end=" ")



#builtin methods in touple
# t6=(1,2,3,4,5,6,7,8)
# # t6[0]=11 #touple is immutable.error dega

# print(min(t6),max(t6),len(t6),sum(t6)) #sabhi ho jayenge


# #sorted()

# print(sorted(t6)) #return list

# #how to make touple function
# t=tuple() #empty tuple object
# # tuple me koi vhi iterable type dene pr usko ye tuple me convert kr dega
# t=tuple([1,2,3])#jese list me condition thi ki iterable hi pas krenge...wese tuple me bhi iterable hi pas hoga
# print(t,type(t))


        #concatination operator
# t1=1,2,4
# t2=4,5,6 
# print(t1+t2) #concatination kr ke single tuple return krega..jese do str,list me bhi concatination ho jata hai...range me nahi hota concatination wo to element access krta hai]

#         #repeatition operator
# print(t1*3)



        #tuple class ke method
#very lomited method in tuple class.bcz tuple mutable nahi hai to bohot si chize to kam hi nhi karegi tuple pe


# jyada function nahi hote hai tuple me
# t2=(2,5,1,6,8,5,6,1,5,3,7)
# print(t2.index(5)) #1 index aayega
# print(t2.count(5)) #5 kitni bar aa raha hai

# SPECIALITY OF TUPLE--->as we know tuple me  modification possible nahi hai immutable hota hai ye so..hame jo data jyada secure rakhna hota hai use hum tuple form me store krwa skte hai...ese case me usefull hota hai tuple.data me changes require hai to use list


# list comprehension ki tarah tuplecomprehension nahi hota hai.but smartly use kiya ja skta hai jese-->

# first n natural number using tuple
# t1=tuple([2*x for x in range(1,int(input("enter n"))+1)])
# print(t1)
# basically list comprehension ko typle function me dal ke type conversion kr liya


