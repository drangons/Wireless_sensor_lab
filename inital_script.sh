#!/bin/sh -w -u



############################################################################Setting Up the Basestation

cp -a /opt/tinyos-2.1.2/apps/tests/deluge/Basestation $HOME/DelugeBasestation
cd $HOME/DelugeBasestation
make iris install,0 mib520,/dev/ttyUSB0 # error redirection here

###########################################################################Install the Golden Image

cp -a /opt/tinyos-2.1.2/apps/tests/deluge/GoldenImage $HOME/GoldenImage
cd $HOME/GoldenImage

##########################################################################prepare the motes
#make iris install,1 mib520,/dev/ttyUSB2
#make iris install,2 mib520,/dev/ttyUSB2
