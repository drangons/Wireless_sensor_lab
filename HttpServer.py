#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import subprocess 
from os import curdir, sep
from scan_programs import Sqltuple

PORT_NUMBER = 8080
SERVER_NAME=''

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  #1. send the list of programs available
  #2. send the compile log file
  #3. send the status file
  #4. send the result file
  def do_GET(self):
    #send the json file
    print 'path'+self.path
    mimetype='text/plain'
    #self.wfile.write("unintialized")
    try:
      if self.path =='/':
        mimetype='text/json'
        j=Sqltuple(1)
        #print j
        self.wfile.write(j)

      elif self.path == '/complie':
        print "in /compile"
        mimetype='text/plain'
        print curdir + sep + self.path+"/example.log"
        f = open(curdir + sep + self.path+"/example.log")
        self.wfile.write(f.read())
        f.close()

      elif self.path == '/status':
        mimetype='text/plain'
        self.wfile.write("/status not implemented !")

      elif self.path == '/result':
        mimetype='text/plain'
        self.wfile.write("/result not implemented !")
      else:
        print "in else"
    except IOError:
      self.send_error(404, 'file not found')
    self.send_response(200)
    self.send_header('Content-type',mimetype)
    self.end_headers()
    return
    #handler for get request
    #get the id of the program to run

  def do_POST(self):
  #expects a id
    return
  #give command to run the program
  #make sure you got the wirte input range, #security
  #subprocess.call(["./install_program.sh",""], shell=True)

  # are the ouptut files written to db? 
    
    
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer((SERVER_NAME, PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
