#scans the file directory for the file INFO to get the the list of programs reday to be installed.
#parameter : Filepath
#Note: the content of the file should be in JSON method.

#!/usr/bin/python

#include the import modules

import sys
import os
import json
from pprint import pprint

#Root path where the programs are stored 
path="../SENSOR_LAB_ASSINGMENTS"

def Sqltuple(jsonobj):
#scan for all files
  files=[]
  for dirname, dirnames, filenames in os.walk(path):
    # print path to all subdirectories first.
    # for subdirname in dirnames:
    #    print os.path.join(dirname, subdirname)

    # print path to all filenames.
    for filename in filenames:
     files.append(os.path.abspath(os.path.join(dirname, filename)))

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.
   #if '.git' in dirnames:
    # don't go into any .git directories.
    #   dirnames.remove('.git')

  #look for the file with name INFO each directory
  i=0
  
  sqltuple=[]
  for f in files:
    if f.endswith("INFO"):
      #read a json structure and form the tuple 
      #print f
      # take the file dir and the JSON data as a tuple
      content=open(f)
      j=json.load(content) # dir(j) is a dict ?
      sqltuple.append((i,j['program name'],j['version'],j['comment'],f[:-5]))
      i=i+1
      content.close()
      
  if jsonobj : 
    print j
    return j

  #Form a list and return it SQl for insertion.

  
  
  for data in sqltuple:
    print data
  
  return sqltuple  

  
