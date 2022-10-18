
#reverse number

def reverse():
    n=int(input("Enter number: "))
    r=0
    n1=n
    while(n>0):
        rem=n%10
        r=r*10+rem
        n=n//10
    print("The reverse number: ",r)     
        
#reverse()
