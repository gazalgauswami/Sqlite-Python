#delete dat
def delete_data():
    import sqlite3
    con=sqlite3.connect('c:\sqlite\one.db')
    e1=int(input('Enter Eid: '))
    con.execute(f'delete from emp where eid={e1}')
    print('data delete succesfully')
    con.commit()
    con.close()
