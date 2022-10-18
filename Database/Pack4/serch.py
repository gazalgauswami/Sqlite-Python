#serch data
def serch_data():
    import sqlite3
    con=sqlite3.connect('c:\sqlite\one.db')
    e1=int(input('Enter Eid: '))
    a=con.execute(f'select * from emp where eid={e1}')
    for i in a:
        print(i[0],"%10s"%i[1],"%10s"%i[2],"%10s"%i[3],"%10s"%i[4],"%10s"%i[5])
