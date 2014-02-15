#Creates a SQLite database and inserts list of programs available for dissemination 
#!/usr/bin/python

#import statements

import sqlite3
from scan_programs import Sqltuple

conn=sqlite3.connect("programs.db")

c=conn.cursor()

#create table

c.execute('''CREATE TABLE programs
             (Id integer, program text, version real, comment test)''')

programs=Sqltuple()

c.executemany('INSERT INTO programs VALUES (?,?,?,?)', programs)             
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
