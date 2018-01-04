import time
import socket 
import sys

class SIP_Socket:

	proxyAddress = None
	proxyPort = None

	@staticmethod
    def SetProxyAddress(address,port):
        SIP_Socket.proxyAddress = address
        SIP_Socket.proxyPort = port

    @staticmethod
    def Listen():
        sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        sock.bind(("0.0.0.0",SIP_Socket.proxyPort))
        while True:
            data, addr = sock.recvfrom(1024)
            

    @staticmethod
    def Send(sipMessage):
    	sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    	sock.sendto(sipMessage, (SIP_Socket.proxyAddress, SIP_Socket.proxyPort))

    @staticmethod
    def getIP(self): 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))
        ip = s.getsockname()[0]
        s.close()
        return ip 
