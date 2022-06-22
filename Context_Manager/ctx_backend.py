from sqlite3 import connect

from matplotlib.style import context 



#Custom Context Manager 
class contextmanager:
    def __init__(self, gen):
        #self.cur = cur
        self.gen = gen 

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self
    def __enter__(self):
        #self.gen = temptables(self.cur)
        self.gen_inst = self.gen(*self.args, **self.kwargs)
        next(self.gen_inst)

    def __exit__(self, *args):
        #Returns next item in an iterator. 
        #Return default value None if there is no next value
        next(self.gen_inst, None)


#Adding generators to call functions in sequence only. 
#Enter can now be executed first and than exit.
def temptables(cur): 
    cur.execute("create table points (x int, y int)")
    print("Create table")
    yield 
    cur.execute("drop table points")
    print("Drop table")

temptables = contextmanager(temptables)

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
    