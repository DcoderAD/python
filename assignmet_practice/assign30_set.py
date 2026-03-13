# print all distinct elements of a list use set to splve this problem
# l=[1,2,3,3,3,5,4,1,1,12,5,5,7,8,1,0,0,0]
# for e in set(l):
#     print(e)


# print two sets from given set one of even and one is odd numbre of set
# s={1,2,3,4,5,6,7,8,9,10,11,12,13,111}
# odd_list=[]
# even_list=[]
# for e in s:
#     if e%2==0:
#         even_list.append(e)
#     else:
#         odd_list.append(e)
# ev=set(even_list)
# odd=set(odd_list)
# print(odd,ev)


                        # or

# s={1,2,3,4,5,6,7,8,9,10,11,12,13,111}
# odd=set()
# even=set()
# for e in s:
#     if e%2==0:
#         even.add(e)
#     else:
#         odd.add(e)
# print(even,odd)


#given a set of five player.make script of all possible pair of two players..
# players = {"Alice", "Bob", "Charlie", "David", "Eve"}
# i=0
# for p1 in players:
#     i+=1
#     for p2 in list(players)[i::]:
#         print(p1,p2)
        

#you have list of candidate some wearing black  hat,some red shoes some both.
# (1) we have list of wearing black hat
# (2) we have another list of wearing red shoes
# (3) firnd out the name of student with both black hat abd red shoes
# candidate={'a','b','c','d','e','f','g','h','i','j','k'}
# black_hat={'a','b','c','h'}
# red_shoes={'a','d','f','i','c'}
# s1=black_hat.intersection(red_shoes)
# print(s1)





#create set of tuple where each tuple has two elements representing dice upper face number.take a number n from the user and generate all possible tuple.in such a way that tuple elements sum to n.
# n=int(input("enter a number"))
# s=set()
# for i in range(1,7):
#     for j in range(1,7):
#         if i+j==n:
#             s.add((i,j))
# print(s)