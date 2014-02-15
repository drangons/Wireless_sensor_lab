#a simple http webserver which prints the list of available programs and accecpts command to dessimate the program.
#The error propogation and returning the output values to the client has to be designed


#!/usr/bin/python 

import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
  
