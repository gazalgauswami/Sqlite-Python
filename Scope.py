#Local scope value
a=5
def testing1():
    a=6
    def testing2():
        a=7
        print(a)
    testing2()
testing1()    

#Enclosed Scope Value
a=5
def testing1():
    a=6
    def testing2():
        
        print(a)
    testing2()
testing1() 

#Glbal Scope Value
a=5
def testing1():
   
    def testing2():
        
        print(a)
    testing2()
testing1() 
