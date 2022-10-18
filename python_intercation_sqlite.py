#python interaction with sqlite3

#connect() method
import sqlite3
con=sqlite3.connect('c:\sqlite\one.db')
print('successfully connected')
#execute() method
#con.execute('create table tblstud (sid,sname,class)')
print('Table create successfully')
for i in range(1,4):
    e1=int(input('Enter sid: '))
    e2=input('Enter sname: ')
    e3=int(input('Enter class: '))
    con.execute(f'insert into tblstud values {e1,e2,e3}')
print('insert data successfully')
#fetchone() method
a=con.execute('select * from tblstud')
b=a.fetchone()
print(b)
#for loop
a=con.execute('select * from tblstud')
for i in a:
    print(i[0],"%20s"%i[1],"%20s"%i[2])
#update data into database
e1=int(input('Enter sid: '))
con.execute(f'update tblstud set class=class+1 where sid={e1}')
print('Update data succesfully')
#fetchall method
a=con.execute('select * from tblstud')
b=a.fetchall()
print(b)
#delete data from database
e1=int(input('Enter sid: '))
con.execute(f'delete from tblstud where sid={e1}')
print('Data deleted succesfully')

