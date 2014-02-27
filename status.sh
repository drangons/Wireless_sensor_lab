#!/bin/sh -w -u

#Deluge limitations

#In addition, Deluge T2 comes with 4 flash volumes by default. However, more volumes can be added, if necessary. 
#There are also some minor details that will be improved in future releases. 



# wrong flags correct it ??

# This script should check the health of the motes and should give the summary of the setup.


# this information should be updated in the db ?

tos-deluge serial@/dev/ttyUSB1:57600 -b # reboot the base station
#Flushing the serial port..
#Checking if node is a Deluge T2 base station ...
#Command sent

tos-deluge serial@/dev/ttyUSB1:57600 -p 2 # ping a specific image slot in the base station

#Flushing the serial port..
#Checking if node is a Deluge T2 base station ...
#Pinging node ...
#--------------------------------------------------
#Currently Executing:
#  Prog Name:   BasestationAppC
#  UID:         0x511F9093
#  Compiled On: Thu Feb 27 15:55:43 2014
#  Node ID:     0

#Stored image 2
#  Prog Name:   BlinkAppC
#  UID:         0x44F17728
#  Compiled On: Tue Feb 11 12:21:31 2014
#  Platform:    iris
#  User ID:     d.siddapurahema
#  Host Name:   ws6
#  User Hash:   0xADF18A57
#  Size:        22464
#  Num Pages:   20
#--------------------------------------------------


tos-deluge serial@/dev/ttyUSB1:57600 -e 2 # erase the memory on the Basestation slot 2
#Flushing the serial port..
#Checking if node is a Deluge T2 base station ...
#ERROR: Unable to erase the flash volume error: 1 data: [] 
#Attempt the workaround for AT45DB...
#Image number 2 erased

# now the image  ping is 
tos-deluge serial@/dev/ttyUSB1:57600 -p 2

#Flushing the serial port..
#Checking if node is a Deluge T2 base station ...
#Pinging node ...
#--------------------------------------------------
#Currently Executing:
#  Prog Name:   BasestationAppC
#  UID:         0x511F9093
#  Compiled On: Thu Feb 27 15:55:43 2014
#  Node ID:     0
#
#No valid image was detected.
#--------------------------------------------------





