from sqlite3 import connect

from matplotlib.style import context 
from contextlib import contextmanager

#Use of Decorator, generator and context manager

#Adding generators to call functions in sequence only. 

@contextmanager
def temptables(cur): 
    cur.execute("create table points (x int, y int)")
    print("Create table")
    try:
        yield 
    finally:
        cur.execute("drop table points")
        print("Drop table")

#with is automatic opening closing the file 
#How can we write our own context manager to create and drop table
with connect('test.db') as conn: 
    cur = conn.cursor()
    with temptables(cur):
        #cur.execute("create table points (x int, y int)") 
        cur.execute("insert into points (x,y) values(1,1)")
        cur.execute("insert into points (x,y) values(1,2)") 
        cur.execute("insert into points (x,y) values(2,1)") 
        for row in cur.execute('select x,y from points'):
            print(row)
        for row in cur.execute('select sum(x*y) from points'): 
            print(row)
        #cur.execute('drop table points')
    