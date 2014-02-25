#!/bin/sh -w -s

# too much of processing, use the python

#Get the argument


# connect to the db and get the program .


#should it takes the motes to be installed as well ?

# now run commands to install the programs and redirect the ouput& error of  the program to the file.

# make sure that at this point that initall_setup.sh is run

# install the program on base station volume
tos-deluge serial@/dev/ttyUSB1:57600 -i 2 build/iris/tos_image.xml allout.txt 2>&1 # 2 is the image slot. Should you clear the image slot after some time . 
#Do you want a clean up script

# dessimate the program in volume 2

tos-deluge serial@/dev/ttyUSB1:57600 -d 2  allout.txt 2>&1

#instruct the remote mote to install the program in volume 2
tos-deluge serial@/dev/ttyUSB1:57600 -dr 2 allout.txt 2>&1


#should you upload the file to the db now in a seperate column ?
