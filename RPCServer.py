import datetime # For time and date function
import socket # for get_ip()
import os
#--------------------------------------------------------------
# Identify this device's IP address as IP -
# so the client can set the IP for the server
#--------------------------------------------------------------
def get_ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except:
		IP = '127.0.0.1' #do not return the default first address as it is the loopback address
	finally:
		s.close()
	return IP
#------------------------------------------------
# Connect to remote service via RPC
#------------------------------------------------
ipAddress = get_ip()
#ipAddress = input("Enter the server's IP address: ")
#------------------------------------------------
# Set the port number
#------------------------------------------------
Service_PortNumber = 10054
#------------------------------------------------
#------------------------------------------------
# Get RPC Package
#------------------------------------------------
from xmlrpc.server import SimpleXMLRPCServer
#------------------------------------------------
#Define the functions to be called
#------------------------------------------------
def is_even(n):
	print("is_even has been called by a client")
	return n % 2 == 0
def square(n):
	print("square(n) has been called by a client")
	return n * n
def add(a,b):
	print("add(a,b) has been called by a client")
	return a+b
def message():
	print("message() has been called by a client")
	return "This is the remote server's message"
def today():
	print("today() has been called by a client")
	today = datetime.datetime.today()
	return today
def find_max (L):
	max = 0
	for x in L:
		if x > max:
			max = x
	return max
def bubbleSort(list):
	listLength = len(list) 
	# Traverse through all listay elements
	for i in range(listLength):
		# Last i elements are already in place
		for j in range(0, listLength-i-1):
			# traverse the lists from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list
def helpRequest():
	helpString = """The API available on """ + get_ip() + """'s TCP Port """ + str(Service_PortNumber) + """ is...
      Bool is_even(int)
      long square(long)
      sum(long,long)
      string message(void)
      dateTime today(void)
      long findMaxValue([long List]
      long sortList([long List])"""
	return helpString
#------------------------------------------------
#Server to listen on local host
# on port 10054
#------------------------------------------------
# server = SimpleXMLRPCServer(("localhost", Service_PortNumber))
server = SimpleXMLRPCServer((get_ip(),10054)) #<< this uses the given address
#------------------------------------------------
"""print("the API available is...")
print("  Bool is_even(int)")52
2
print("  long square(long)")
print("  long sum(long,long)")
print("  string message(void)")
print("  dateTime today(void)")
print("  long findMaxValue([long List])")
print("  long sortList([long List])")
print("Listening on port 10054...")"""
print(helpRequest())
print("This server's Process id: "+  str(os.getpid()))
print("Listening for client requests...")
#------------------------------------------------
# Register the functions that the server can handle
# This is the API for this server
# syntax for the API code...
# server.register_function(name of function on this server, "name of function in API")
#------------------------------------------------
server.register_function(is_even, "is_even")
server.register_function(square, "square")
server.register_function(add, "sum")
server.register_function(message, "message")
server.register_function(today, "today")
server.register_function(find_max, "findMaxValue")
server.register_function(bubbleSort, "sortList")
server.register_function(helpRequest, "help")

#------------------------------------------------
#Set the server to listen on the given port
#------------------------------------------------
server.serve_forever()
