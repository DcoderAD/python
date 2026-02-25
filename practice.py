
#if elif else ,single line else if , nesting
#a=int(input("Enter your marks"))
# if 90<a<=100:
#     print("A")
# elif 80<a<=90: #80 exclude ho raha hai but 90 include hai
#     print("B")
# elif 70<a<=80:
#     print("C")
# elif 60<a<=70:
#     print("D")
# elif 50<a<=60:
#     print("E")
# elif 0<a<=50:
#     print("F")
# else:
#     print("Invalid marks")


# a=int(input("Enter a number"))
# result="positive" if a>0 else "negative" #yaha is expression ka koi ek output aayega jo result me store ho jayega

# or
 
# print("positive" if a>0 else "negative")

# --------------------nested if else----------
a=int(input("Enter a number"))
if a>0:
    if a>10:
        code1
    else:
        code2 

else: 
    if a<-10:
        code1
    else:
        code2 