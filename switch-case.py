abc='abc'#-->ye hamne eval and string me hone wale conflict ko resolve krne ke liye likha hai
"""
so eval(input()) me strint input krne pe input function string hi return krta hai and then eval function use  " " hata ke evaluate krne ki try krta hai to use lagta hai wo string nahi variable ka nam hai and esa kooi variablee to exist krta nahi hai to error aa jati hai
"""
x=eval(input("Enter your input"))#eval string ke sath problem krta hai
match x:
    case 30:
        print("int")
    case 1.2:
        print("float")
    case True:
        print("Bool")
    case 3+4j:
        print("complex")
    case "abc":
        print("string")
    case None:
        print("none")
    case _:#kooi case match nahi hoga tab ye chalega.ts like default case in other language like c/c++
        print("invalid")

#match-case soft kayword hai means the can be used as variable name too.only in match case format they are considered as keywords

#when to use match case??
#jab bohot se options me se 1 select krna ho to nesting krne se better hai match case use kre
"""agar do case ke constant same hai to use duplicate case kahenge python me duplicate case error nahi deta hai other language me error dega.python me case matching first se start hoti hai agar do case same hai to ko pahle encounter hoga use concider kar liya jayega baki ke case chk hi nahi hote hai.
"""


# match case with if condition
print("Enter username")
username=input()
print("Enter password")
password=int(input())
match password:
    case 1234 if username=='rahul':
        print("monday")
    case 2345 if username=='rohit':
        print("tuesday")
    case 1000 if username=="admin":
        print("webnesday")
    case password if username=='guest':#pasword variable hai jo yaha nahi likh sakte hai but condition ke sath esa likha ja sakta hai.is case me pasword ..pasword se match hoga and print kar hi dega   username kuchh bhi ho.
        print("sunday")