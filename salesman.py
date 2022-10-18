


#3.1 create database
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

#3.2 create table salesman
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
con.execute('create table Salesman (sid primary key,name text ,city text,commision real)')
print("Table create Succusfully")

#3.3 insert data into table
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

con.execute('insert into Salesman values (5001,"Mohan Patel","Anand",0.15)')
con.execute('insert into Salesman values (5002,"Nail Shah","Surat",0.13)')
con.execute('insert into Salesman values (5005,"Preet Vyas","Ahmedabad",0.11)')
con.execute('insert into Salesman values (5006,"Jeevan Mehta","Navsari",0.14)')
con.execute('insert into Salesman values (5003,"Paul Adam","Nadiad",0.12)')
con.execute('insert into Salesman values (5007,"Ramesh Patel","Surat",0.13)')
print('data insert succesfully')
con.commit()
con.close()

#3.4 Display 1 and 2 record ussing fetchone() method
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

a=con.execute('select * from Salesman')
b=a.fetchone()
print(b)
c=a.fetchone()
print(c)

con.commit()
con.close()

#3.5 Display data using fetchall() method

import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute('select * from Salesman')
d=a.fetchall()
print(d)

con.commit()
con.close()

#3.6 Display 4 and 5 record using fetchall() method
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute('select * from Salesman')
d=a.fetchall()
print(d[3][0]," ",d[3][1]," ",d[3][2]," ",d[3][3])
print(d[4][0]," ",d[4][1]," ",d[4][2]," ",d[4][3])

con.commit()
con.close()

#3.7 Display data without using fetchone() and fetchall() method
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute('select * from Salesman')
for i in a:
    print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])
con.commit()
con.close()

#3.8 Display the record od salaesman who are living insurat city
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute('select * from Salesman where city="Surat"')

for i in a:
    print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])              

con.commit()
con.close()

#3.9 Display record of salesman whose name consists letter "M"
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute('select * from Salesman where name like "M%"')

for i in a:
     print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])              

con.commit()
con.close()

#3.10 Display record of salesman whosw commision is range of 0.11 to 0.13
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute(" select * from Salesman where commision between 0.11 and 0.13")

for i in a:
     print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])

con.commit()
con.close()

#3.11 Display records of salesman of Anad and Navsari city

import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')
a=con.execute("select * from Salesman where city in ('Anand','Navsari')")

for i in a:
     print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])

con.commit()
con.close()

#3.12 Take Salesman's SID from user and display his detail

import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

e1=int(input("Enter SID: "))
a=con.execute(f' select * from Salesman where sid={e1} ' )

for i in a:
     print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3])


con.commit()
con.close()


#3.13 Modify the commision of 5006 to 0.15
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

a=con.execute('update Salesman set commision=0.15 where sid=5006')
print('Update Successfully')
con.commit()
con.close()

#3.14 Modify the city to Bharuch Whose commision is 0.13
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

a=con.execute('update Salesman set city="Bharuch" where 0.13')
print('Update Successfully')
              
con.commit()
con.close()

#3.15 Delete the record of 5007
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

#a=con.execute('delete from Salesman where sid=5007')
print('Delete data succesfully')
con.commit()
con.close()

#3.16 Delete the reecord of salaesman of bharuch city
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

a=con.execute('delete from Salesman where city="Bharuch"')
print('Delete data succesfully')

con.commit()
con.close()

#3.17 insert three record into salesman tables as per user's input
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

for i in range(1,4):
    e1=int(input("Enter sid:  "))
    e2=input("Enter Name:  ")
    e3=input("Enter city:  ")
    e4=input("Enter commision:  ")
    a=con.execute(f'insert into Salesman values {e1,e2,e3,e4}')
print("Data insert succesfully")

con.commit()
con.close()

