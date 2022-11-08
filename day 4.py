"""
#write a program to
display india if 8<3
display AUS if 4<3
display EU if 9<3
else
usa
"""



#algorithm
#Step1
#put a condition to check 8<3 if condition is True then only print india
#step2
#put a condition to check 4<3 if condition is true then only prit AUS
#step 3
#put a condition to check 9<3 if conditon is true then only print EU
#step 4
#if it doesnt support the above condition
#else print USA


if 8<3:
    print("India")
elif 4<3:
    print("AUS")
elif 9<3:
    print("EU")
else:
    print("USA")


a=50
b=30
if a==b:
    print("a is equal to b")

elif b>a:
    print("b is greater than a")

elif a!=b:
    print("a is not equal to b")
else:
    print("a is greater than b")







if 3==4:
    print("3 id equal to 4")
elif 4<3:
    print("3 greater than 4")
elif 4>3:
    print("4 is greater than 3")
else:
    print("3 is equal to 4")



if 3!=4:
    print("F")
elif 4>5:
    print("S")
elif 3<4:
    print(5)
else:
    print("A")










#step1
#Define mylist[1,2,3,4,5]
#step2
#put condition to check if 2 is in mylist      
#step3
#print 4th index number value
#step4
#if condition not satisfies else print zero[0]    



mylist=[1,2,3,4,5,6]
if 2 in mylist:
    print(mylist[4])
else:
    print(0)


mylist=["a","b","c","d","e","f"]
if "a" in mylist:
    print("mum")
else:
    print(0)







mytuple=("umbrella","raincoat","rain")
if "umbrella" in mytiple:
    print(mytuple)
else:
    print(50)



mytuple=(12,14,16,18,20)
if 13 in mytuple:
    print:(mytuple)
else:
    print(5)

mytuple=(10,15,20,25,30)
if 25 in mytuple:
    print(mytuple[4])
else:
    print("name")


myset={10,12,14,16,18,20}
if 12 in myset:
    print(myset)
else:
    print(1)


myset={10,12,14,16,18,20}
print(myset)



myset={1,2,3,4,5}
print(myset)


mydict={12:60,"height":5, (1,2,3):5}

if "height" in mydict:
    print(type(mydict))
else:
    print(5)


mydict={12:60,"height":5, (1,2,3):5}

if "mumbai" in mydict:
    print(type(mydict))
else:
    print("sagar")



mydict={12:60,"height":5, (1,2,3):5}

if "mumbai"  not in mydict:
    print(type(mydict))
else:
    print("sagar")

"""
#write a item to print list item and wait for 3sec for each item to be printed


#Algorithm
#step1- import required library for sleep time purpose
#    (import time)
#Apply loop
#step 3
#print item
#step 4
#wait for 3sec.
    



#ex:
    
"""
import time
for item in [1,2,3,4]:
    print(item)
    time.sleep(3)

import time
for item in ["a","b","c"]:
    print(item)
    time.sleep(2)    

        

import time
for item in "India is a beautiful country to live":
    print(item)
    time.sleep(2)
    
import time
for item in (1,2,3,4,5,6):
    print (item)
    time.sleep(2)

import time
for item in {"a":500, (10,20):100}:
    print(item)
    time.sleep(1)

import time
for item in {(1,2,3), "India", }):
    print(item)
    time.sleep(2)


import time
for item in (1,2,3):
    print(item)
    time.sleep(.5)








#EX: write a programme divisible by 3 from range 1lakh
#Range steps
#1 import require library for time requirements
#2 Define mylist to 1lakh range
#3 apply loop over the list of items
#4 put the condition for the item to divisible by 3
#5 print the item condition value if condition is true
#6 keep 2 sec delay    
    

import time
mylist=(range (100000))
for item in mylist:
    if item %3==0:
        print(item)
        time.sleep(1)
# write a program to print even or odd numbers in the list of 1-15 with 2sec delay 

#import require library for time delay
#define mylist to 15 range
#loop over the list of items
#put the condition tp check the number divisible by2 or not
#if condition is true, it is a even number
#print item value
#else print odd number,
#print the item value
#keep 2 sec delay


import time
mylist= (range (15))
for item in mylist:
    if item  %2==0:
        print("even number is", item)
        time.sleep(2)
    else:
        print("odd numbers is", item)
        time.sleep(2)

 
#Number divisible by 3 and 5 in the range of 50
        



import time
mylist=range (50)
for item in mylist:
    if item %3==0:
        print(item)
        time.sleep(2)

import time
mylist=range(30)
for item in mylist:
    if item %4==0:
        print(item)
        time.sleep(1)



import time
mylist=range(15)
for item in list:
    if item %2==0:
        print(item)
    else:
        print(item)
        time.sleep(.5)
    
         


import time
mylist=range (50)
for item in mylist:
    if item %25==0:
        print("mylist with %25 is",item)
        time.sleep(2)










   

if 3>4:
    print(5)
elif 3<4:
    print(6)
elif 3==4:
    print(t)
else:
    print(8)




    
import time
for item in (1,2,3,4,5):
    print("mylist is", item)
    time.sleep(2)




import time
for item in[1,2,3,4]:
    print(item)
    time.sleep(1)



if 3!=4:
    print("F")
elif 4>5:
    print("S")
elif 3<4:
    print(5)
else:
    print("A")





import time
for item in {(1,2,3), "India", 5 }:
    print(item)
    time.sleep(2)



import time
mylist= range(15)
for item in mylist:
    if item%2!=0:
        print(item)
        time.sleep(2)
    else:
        print(item)
        time.sleep(2)











    
