#update data
def update_data():
    import sqlite3
    con=sqlite3.connect('c:\sqlite\one.db')
    e1=int(input('Enter Eid: '))
    con.execute(f'update emp set salary=salary+100 where eid={e1}')
    print('data update succesfully')
    con.commit()
    con.close()
