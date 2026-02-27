"""list comprehension"""
#use for precise coding
# suppose we want to generate the elements of a list using some logic.like list of 100 natural number.100 kon type krega...use list comprehension
# niche likha expression list ka element create karega.leki jis logic se ye generate karega usse 1 hi element generate hoga.jyada generate karwane ke liye loop use kre.for looop use kre while nahi.

# listObject=[expression]




# listObject=[expression for variable in iterable ]
                        # &
# listObject=[expression for variable in iterable if condition ]
                        
                        # or

                        
# ye upr likhi line similar hai.upar ek line me pricisly likh diya-->
# listObject=[]
# for variable in iterable:
#     if condition: 
#         listObject.append(expression)


# print first 10 even number list comprehension
# list=[e for e in range(2,21,2)]
# print(list)


                # or


# 1 to 21 20 element aayenge but if condition ko jo satisfy krega wo hi print hoga
# list=[x for x in range(1,21,1) if x%2==0]
# print(list)



# list=[x**2 for x in range(1,21,1) if x%2==0]
# print(list)
