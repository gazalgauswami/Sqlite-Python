#(A) Addition of two numbers
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print("Addition of two number is: ",a+b)

    
 #(B) Subtraction of two numbers
def sub(a,b):
    print("substraction of two number is: ",a-b)
    
 #(C) Multiplication of Two numbers
def multi():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    return(a*b)
    
 #(D) Division of two numbers
def div(a,b):
    return(a/b)
 #(E) Greatest of two numbers
def great():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    if(a>b):
        print("Greasest number is a:  ",a)
    else:
        print("Greatest number is b:  ",b)
 #(F) Smallest number from two numbers.
def small():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    if(a<b):
        print("Smallest number is a:  ",a)
    else:
        print("Smallest number is b:  ",b)
 #(G) Simple Interest
def si():
    p=int(input("Enter p:  "))
    r=int(input("Enter r:  "))
    n=int(input("Enter n:  "))
    print("Simple interest is:  ",(p*r*n)/100)
