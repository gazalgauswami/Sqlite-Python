#armstrong number

def armstrong():
    n=int(input("Enter number: "))
    sum=0
    n1=n
    while(n1>0):
        r=n1%10
        sum=r*r*r
        n1=n1/10  
    if n==sum:
        print("armstrong number")
    else:
        print("Not armstrong number")

