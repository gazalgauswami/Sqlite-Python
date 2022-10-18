from Calculator import *

while True:
    print("1.Addition\n2.Substraction\n3.multiplication\n4.Division\n5.Greatest number\n6.Smallest Number\n7.Simplae interst\n8.exit ")
    ch=int(input("\n Enter Your Choise: "))

    if ch==1:
           add()
    elif ch==2:
         a=int(input("Enter a: "))
         b=int(input("Enter b: "))
         sub(a,b)
    elif ch==3:
        print("Multiplication of two number: ",multi())

    elif ch==4:
        a=int(input("Enter a: "))
        b=int(input("Enter b: "))
        print("Division of two number:  ",div(a,b))

    elif ch==5:
        great()

    elif ch==6:
        small()

    elif ch==7:
        si()

    elif ch==8:
        break

    else:
        print("Sorry, you have wrong choise")
        
        
    
