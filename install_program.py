#!/usr/bin/python

# connect to the sqlite db

import sqlite3

conn=sqlite3.connect("programs.db")

c=conn.cursor()

id=1
c.execute("Select * from progrmas where id=?", id)

r=c.fetchone()
# get the program path 

path=r['path']
program_name=r['program']

#Go to the directory

os.chdir(path) # possible exception.


f = open('compile_log', 'w')

# install the program on base station volume
result=subprocess.call(['tos-deluge',' serial@/dev/ttyUSB1:57600', '-i <volume>',' build/iris/tos_image.xml'],stdout=f, stderr=subprocess.STDOUT, shell=True) #allout.txt 2>&1 # use the subprocess module here

if result !=0:
  pass


# dessimate the program in volume 2

result=subprocess.call(['tos-deluge',' serial@/dev/ttyUSB1:57600',' -d 2 '] ,stdout=f, stderr=subprocess.STDOUT, shell=True )

if result !=0:
  pass
#instruct the remote mote to install the program in volume 2
result=subprocess.call(['tos-deluge',' serial@/dev/ttyUSB1:57600',' -dr 2 '], stdout=f, stderr=subprocess.STDOUT, shell=True) 

if result !=0:
  pass
#create a new table in the db and insert the text file ??
c.execute('''CREATE TABLE compile_log
             (Id integer,data blob)''')

#what is the advantage of putting it in the db ?, can you just send the file?             
with open("allout.txt", "rb") as input_file:
    ablob = input_file.read()
    cursor.execute("INSERT INTO notes (id, file) VALUES(0, ?)", [sqlite3.Binary(ablob)])
    conn.commit()

#to get the file from db and write back   
with open("Output.bin", "wb") as output_file:
    cursor.execute("SELECT file FROM notes WHERE id = 0")
    ablob = cursor.fetchone()
    output_file.write(ablob[0])

c.close()
conn.close()


