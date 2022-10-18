#5.1
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

con.execute("create table customer1(cid primary key,cust_name,grade)")
print("Table create succesfully")

#5.2
con.execute(' create trigger trg_grade after insert on customer begin select case when new.grade>100 and new.grade<500 then raise(abort,"Grade is between 100 and 500") else raise(abort,"Grade is not between 100 and 500") end; end;')
print("Trigger create succesfully")

#5.3
con.execute("insert into customer1 values('C1','Mohit Patel',100)")
con.execute("insert into customer1 values('C2','Geeta Vyas',200)")
con.execute("insert into customer1 values('C3','Jaya Patil',100)")
con.execute("insert into customer1 values('C4','Vishal Gohel',300)")
con.execute("insert into customer1 values('C5','Kartik Goyenka',200)")
con.execute("insert into customer1 values('C6','Meera Prajapati',100)")
con.execute("insert into customer1 values('C7','Veer Vyas',300)")
con.execute("insert into customer1 values('C8','Maya Mehta',200)")
print("insert data succesfully")
con.commit()

#5.5
a=con.execute("select distinct grade from customer1")
b=a.fetchall()
print(b)

#5.6
a=con.execute("select *,(case when grade=100 then 5000 when grade=200 then 10000 else 15000 end)as bonus from customer1")
b=a.fetchall()
for i in b:
    print(i)

#5.7
e1=int(input("Enter Grade: "))
a=con.execute(f"select * from customer1 where grade={e1}")
b=a.fetchall()
for i in b:
    print(i)
    
#5.8
e1=input("Enter Letter: ")
a=con.execute(f"select * from customer1 where cust_name like '{e1}%'")
b=a.fetchall()
for i in b:
    print(i)
 
#5.9
e1=input("Enter Cid: ")
a=con.execute(f"delete from customer1 where cid={e1}")
print("Data delete succefully")

#5.10
e1=input("Enter Cid: ")
a=con.execute(f"update customer1 set grade=grade+50 where cid={e1}")
print("Data update succesfully")

#5.11
for i in range(1,4):
    e1=input("Enter cid: ")
    e2=input("Enter Name: ")
    e3=int(input("Enter grade: "))
    con.execute(f"insert into customer1 values {e1,e2,e3}")
print("Data insert succesfully")

#5.12
e1=input("Enter city: ")
a=con.execute(f"select * from Salesman where city={e1}")
b=a.fetchall()
for i in b:
    print(i)

#5.13
e1=int(input("Enter Purchase Amount: "))
a=con.execute(f"select * from order1 where pur_amt>{e1}")
b=a.fetchall()
for i in b:
    print(i)
    
#5.14
e1=int(input("Enter Sid: "))
a=con.execute(f"select * from Salesman where sid={e1}")
b=a.fetchall()
for i in b:
    print(i)

