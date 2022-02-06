import datetime
import socket # for get_ip()
import os
#------------------------------------------------
# Get RPC Package
#------------------------------------------------
import xmlrpc.client
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
# Connect to remote service via RPC
#------------------------------------------------
ipAddress = get_ip()
#ipAddress = input("Enter the server's IP address: ")
Service_PortNumber = 10054
fullAddress = 'http://'+ipAddress+':'+ str(Service_PortNumber)  + '/'
print('----------------------------------------')
remoteServer = xmlrpc.client.ServerProxy(fullAddress)
#------------------------------------------------
# local function's 'message()'
#------------------------------------------------
def message():
	return "This is this node's message"
#------------------------------------------------
# Calling remote functions
#------------------------------------------------
print("Process id: "+  str(os.getpid()))
print("using remoteServer.help() returns\n %s" % remoteServer.help())
print('----------------------------------------')
print(' Using the functions gives...')

print('----------------------------------------')
print ("Bool is_even(3) returns: %s" % str(remoteServer.is_even(3)))
print ("Bool is_even(6) returns: %s" % str(remoteServer.is_even(6)))
print ("square(3) returns: %s" % str(remoteServer.square(3)))
print ("square(9) returns: %s" % str(remoteServer.square(9)))
print ("add(8,5) returns: %s" % str(remoteServer.sum(8,5)))
arrayOfNumbers = [1,2,7,3,4.3,8,13,5,4]
print("findMaxValue %s"  % arrayOfNumbers, " returns: %s"% str(remoteServer.findMaxValue(arrayOfNumbers)))
print("sortList(%s)"  % arrayOfNumbers, " returns: %s"% str(remoteServer.sortList(arrayOfNumbers)))

#-----------------------------------------------
# Showing local and remote versions of the same function name
#------------------------------------------------
print("message() returns: %s" % message())
print("remoteServer.message() returns: %s" % remoteServer.message())

#------------------------------------------------
# Receiving time/date data
#------------------------------------------------
timeNow = remoteServer.today()
converted = datetime.datetime.strptime(timeNow.value, "%Y%m%dT%H:%M:%S")
print("remoteServer.today() returns %s" % timeNow)
print("Formatted remoteServer.today(): ", converted)
