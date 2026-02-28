"""str methods"""
#built in methods works universally.but class ke function specific us type ko handle krne ke liye banaye gaye hote hai
# s1="ajay education services"

                #INDEX FUNCTION
# print(s1.index('i')) #sbse pahle i kaha milega in index.
# print(s1.index('z'))#error dega z nahi hai string me
# print(s1.index('edu'))# 'e' ka index return karega



                #COUNT FUNCTION
# print(s1.count('a')) #'a' ki total occurence dega
# print(s1.count(' ')) #' ' space count dega


                #STARTSWITH & ENDSWITH
# print(s1.startswith('aja'))#True or false me ans dega
# print(s1.endswith('abc'))  #true or false me ans dega

                #ISDIGIT
# there are so meny function of isupper...etc check them too....just by righting is..it will show you
# we cant change in original string.
# s1="ajay education services"
# s2='1234' #isdigit True
# s3='a12345'#isdigit False
# print(s2.isdigit())#truee
# print(s3.isdigit())#false 
# print(s2.isalpha())
# print(s3.isalnum())#'a12345' alphabate+number :True
# print(s1.upper())#print upper case but no change in original string.upper new string bana ke us object ko return kr raha hai original will be the same
# print(s1)
# s4="AJAY"
# print(s4.lower())#no change in the original s4 string
# print(s4)
# print(s4.islower())#"AJAY" not lower so: false

# print(s4.replace('A','J'))#A anywhere in the string will be replaced by j.2 chize pass kr rhe hai first place pe wo alphabate jise replace krna hai and second pe jisse replace krna hai wo alphabate likhenge using ,(again no change in the s4 string .its just returning a new string with all the modifications)

        #some important function
            # split() function 
#split func always return list of string
#split me hum split criteria dete hai jo   ' ' , ya koi sub string bhi ho sakti hai jiske base pe hum string ko split krwate hai
s1="ajay education services"
# print(s1.split(' '))#' ' space ke basis pe split kr rhe hai.jaha jaha space hoga waha se string ko tod dega.jese s1 me 2 sapace hai 3 words ki ek list return ho jayegi.
# space ko remove kar dega
# print(s1.split('a'))#'a' ke besis pe devide krega and sabhi a remove ho jayenge baki sab print hoga



                #join() function
#ye just opposite work krta hai split() function ke
# kisi list ke sabhi elements ko join kar ke ek single string banane ke liye join() use kre
# jo character aap select karoge wo ho join method ko call karega.jese ' '.join(list) me space se string join krwayenge
# s="mysirg education services"
# l=s.split(' ')# give a list of 3 str element
# print(l)
# s1=' '.join(l)#list item will be join by ' '
# s2=' hello '.join(l)
# print(s1)
# print(s2)


            #format() function
a,b=10,20
# print usin print
print("sum of",a,"and",b,"is",a+b)
#print using format spacifire  not recommanded---> 
# xxxxx print("sum of %d & %d is %d"%(a,b,a+b)) xxxxx#dont use it

#print using format function
print("sum of {} and {} is {}".format(a,b,a+b))#use this one 
#each {}{}{} me lagatar a,b,a+b jayega....but order change krwana ho print me b,a,a+b ya a+b,b,a to {}{}{} me index number de sakte ho format(a,b,a+b) ka jo 1 se start hoga
print("sum of {2} and {1} is {0}".format(a,b,a+b))