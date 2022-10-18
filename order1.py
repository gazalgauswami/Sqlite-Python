
#4.1
import sqlite3
con=sqlite3.connect('C:\sqlite\one.db')

#con.execute('create table order1(oid number primary key,pur_amt number,ord_date text,sid number references Salesman (sid))')
print('Table create succesfully')
#4.2
#con.execute(' create trigger trg_amount before insert on order1 begin select case when new.pur_amt>1000 then raise(abort,"Purchase Amount is More Than 1000") when new.pur_amt<1000 then raise(abort,"Purchase Amount is More Than 1000") else raise(abort,"Purchase Amount is M1000") end; end;')
print('create trigger succesfully')
                               
#4.3
con.execute("insert into order1 values(1,12000,'2020-12-05',5001)")
con.execute("insert into order1 values(2,42000,'2020-12-20',5002)")
con.execute("insert into order1 values(3,2000,'2021-02-02',5005)")
con.execute("insert into order1 values(4,14000,'2021-03-23',5005)")
con.execute("insert into order1 values(5,23000,'2021-04-15',5003)")
con.execute("insert into order1 values(6,33000,'2021-05-20',5001)")
con.execute("insert into order1 values(7,32000,'2021-06-22',5003)")
con.execute("insert into order1 values(8,23500,'2021-07-01',5003)")
con.execute("insert into order1 values(9,43000,'2021-07-05',5001)")
con.execute("insert into order1 values(10,12000,'2021-07-05',5002)")
print('data insert succesfully')                                  

#4.5
a=con.execute("select * from order1 order by pur_amt")
b=a.fetchall()
for i in b:
    print(i)

4.6
a=con.execute("select * from order1 limit 5")
b=a.fetchall()
for i in b:
    print(i)


4.7 
a=con.execute("select * from order1 where strftime('%m',ord_date)='12' ")
b=a.fetchall()
for i in b:
    print(i)

4.8
a=con.execute("select * from order1 where pur_amt between 10000 and 20000")
b=a.fetchall()
for i in b:
    print(i)
   
4.9
a=con.execute("select name,city,o.* from Salesman s,order1 o where s.sid=o.sid")
b=a.fetchall()
for i in b:
    print(i)

4.10
a=con.execute("select sid,count(pur_amt)as total_purchase from order1 group by sid")
b=a.fetchall()
for i in b:
    print(i)

4.11
a=con.execute("select *,(case when sid in (5001,5002) then 'A' when sid in (5003,5005) then 'B' else 'C' end)as class from order1")
b=a.fetchall()
for i in b:
    print(i)

4.12
a=con.execute("select order1.*,commision  from salesman , order1 where salesman.sid=order1.sid")
b=a.fetchall()
for i in b:
    print(i)
   
4.13

a=con.execute("select * from Salesman where sid not in(select sid from order1)")
b=a.fetchall()
for i in b:
    print(i)
''  
4.14
a=con.execute("select * from order1 order by ord_date")
b=a.fetchall()
for i in b:
    print(i)
    
4.15
e1=input("Enter date e1: ")
e2=input("Enter date e2: ")
a=con.execute(f"select * from order1 where ord_date between {e1} and {e2}")
b=a.fetchall()
for i in b:
    print(i)


