#display data
def display_data():
    import sqlite3
    con=sqlite3.connect('c:\sqlite\one.db')
    a=con.execute('select * from emp')
    for i in a:
        print(i[0],"%30s"%i[1],"%30s"%i[2],"%30s"%i[3],"%30s"%i[4],"%30s"%i[5])
