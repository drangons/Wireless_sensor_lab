#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8080
SERVER_NAME=''

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
	  #send the json file
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		#check the path of the request. If its on /results then send the output of the file 
		self.wfile.write("Hello World !")
		return
  def do_POST(self):
    #expects a id
    
    #give command to run the program
    
    
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
