#insert data
def insert_data():
    import sqlite3
    con=sqlite3.connect('C:\sqlite\one.db')
    #con.execute('create table emp(eid,name,salary,post,gender,jdate)')
    print('table create succesfully')
    con.execute('insert into emp values (101,"Gazal Gauswami",25000,"Accountant","Female","2021-02-02")')
    con.execute('insert into emp values (102,"Pawan Gosai",15000,"CEO","Male","2020-07-15")')
    con.execute('insert into emp values (103,"Meera Mehta",20000,"Boss","Female","2019-08-19")')
    con.execute('insert into emp values (104,"Kejal Goyani",18000,"Clarck","Female","2018-06-08")')
    con.execute('insert into emp values (105,"Om Prkash",50000,"Hr","Male","2017-06-16")')
    print('Data insert succesfully')
    con.commit()
    con.close()                
