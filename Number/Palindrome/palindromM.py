#palindrom number
def palindrom():
    n=int(input("Enter number: "))
    n1=n
    r=0
    while(n>0):
        rem=n%10
        r=r*10+rem
        n=n//10
    if(n1==r):
        print("Palindrom number")

    else:
        print("Not Palindrom number")
#palindrom()
