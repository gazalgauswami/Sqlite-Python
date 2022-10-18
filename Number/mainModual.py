from Reverse.reverseM import *
from Palindrome.palindromM import *
from Armstrong.armstrongM import *


print("1.reverse number 2.palindrom number 3.Armstrong number\n")
ch=int(input("Enter Choise: "))

if ch==1:
    reverse()

elif ch==2:
    palindrom()

elif ch==3:
    armstrong()

else:
    print("You Have Wrong Choise")
