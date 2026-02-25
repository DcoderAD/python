"""agar while ki natural life puri hogi means condition false ho jayegi tabhi else part chalega nahi to nahi chalega """

i=1
while i<=10:
    print(i)
    x=int(input("Enter a number"))
    if x%2==0:
        break
    """agar user first time pe hi even enter krega to break ho jayega or loop ko to 10 bar chalna tha but 1 bar chala or break kr ke bahar aa gaya means loop ki normal life puri nahi hui so ab else ka code nahi chalega"""
    i+=1
else:
    print("you are in else",i)
print("end of code")