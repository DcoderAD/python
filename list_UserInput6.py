"""user input in list"""
# there are multiple way to user input in list





# list me user se element input kese le?
# 1st method
# l=[]
# n=int(input("how many number u want in list\n"))
# print("Enter",n,"numbers now:")
# #number enter krte time , se seprate kroge to accept nahi karega.uske liye alag method hai
# # print("Enter %d numbers:"%(n))#same line hai upr jesi 
# for i in range(n):#10 number ki index 0-9 hogi
#     l.append(int(input()))
# print(l)




# print("Enter number saperated by ,")
# a=input()
# print(a)
"""
bina split kiye to ye ek single string print karega 12,23,34 isme number and coma sabhi string ke pard hai na ki integer .so string class ke split() function ko use krenge
"""
# print("Enter number saperated by ,")
# a=input()   #'12 ,23 ,34 ,45 ,55'
# l=a.split(',')#'12','23','34','45','55' 
# print(l)
"""( )me split krne ka basis likhe, upar , use kiya hai to ab wo sting ka part nahi hai wo split krne ka criteria ban gaya hai and single string  '12 ,23 ,34 ,45 ,55' ko comma ne  '12','23','34','45','55' total 5 strings me tod diya hai.and split function hamesha list of string return karega kyuki string class ka hi function hai.----> ['12','23','34','45','55'] then you convert it into integer."""





# print("Enter number saperated by ,")
# a=input()   #'12 ,23 ,34 ,45 ,55'
# l=a.split(',')#'12','23','34','45','55' 
# l1=[]
# for e in l:
#     l1.append(int(e))
# print(type(l1))




"""or bhi easy way hai isko krne ka,single line me code ban jayega using list comprihension :)"""
print("Enter number saperated by ,")
# input --> '12 ,23 ,34 ,45 ,55'
l1=[int(x) for x in input("Enter num").split(',')]
print(l1)