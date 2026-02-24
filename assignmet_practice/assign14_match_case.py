#check if number is 3 digit number
# n=int(input("Enter number"))
# match n:
#     case 1 if 100<=n<=999:
#         print("its a 3 digit number")
#     case _:
#         print("not a 3 digit number")



#if number is positive ,negative,zero
# a=int(input("Enter a number"))
# match a:
#     case a if a>0:
#         print("Positive") 
#     case a if a<0:
#         print("negative")
#     case a if a==0:
#         print("zero")
#     case _:
#         print("none of above")


#4 options 1.odd even 2.positive non negative 3 simple intrest
# 4 area of circle
# while 1:   
#     print("1.Odd Even")
#     print("2.Positive or non positive")
#     print("3.Simple Intrest")
#     print("4.Quadratic Equation ")
#     print("5.Exit the program")

#     a=int(input("Enter your choice\n"))
#     match a:
#         case 1:
#             print("Enter a number")
#             n=int(input())
#             print("Even" if n%2==0 else "odd" "")
#             continue
#         case 2:
#             n=int(input("Enter a number"))
#             print("positive" if n>0 else "negative ")
#             continue
#         case 3:
#             print("Enter principle,intrest,time")
#             P,I,T=int(input()),float(input()),int(input())
#             print(P*T*I/100)
#             continue
#         case 4:
#             print("Enter the value of a,b,c")
#             a,b,c=int(input),int(input),int(input)
#             r1=(-b+(b*b-4*a*c)**0.5)/2*a
#             r2=(-b-(b*b-4*a*c)**0.5)/2*a
#             print("Roots are", r1 ,"and", r2)
#             continue
#         case 5:
#             print("!! thank you !! for using my program ")
#             break
            
#         case _:
#             print("invalid choice")
#             continue


#user enter data if it is int float complex and bool print monday,tuesday,wedneday,thursday
# a=eval(input("Enter a type of dat above explained"))
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
#         print("str with eval is a unique case")
#     case _:
#         print("none")


#enter string print  different output if str part of "mysirg","education","services"
# a=input("Enter a string")
# match a:
#     case a if "mysirg" in a:
#         print("monday")
#     case a if "education" in a:
#         print("tuesday")
#     case a if "services" in a:
#         print("wednesday")
#     case _:
#         print("none")