import threading
import socketserver
from Katari.sip import SipMessage




class UDPSipServer(socketserver.DatagramRequestHandler):

    application = None


    def handle(self):
        datagram = self.rfile.read()
        message = SipMessage(datagram)
        UDPSipServer.application.socket = self.request
        UDPSipServer.application.client = self.client_address
        UDPSipServer.application._server_run(message)


    @staticmethod
    def start_server(ServerAddress,applcation):
        UDPSipServer.application = applcation
        UDPServerObject = socketserver.ThreadingUDPServer(ServerAddress, UDPSipServer)
        UDPServerObject.serve_forever()











#class SipServer:
#
#
#    def __init__(self, host, port):
#        self.host = host
#        self.port = port
#        self.application = None
#        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#        self.socket.bind((self.host,self.port))
#        self.session_table = SipSessionTable()
#
#
#    def start(self):
#        """
#        Starts the listener method
#        :return:
#        """
#        self.listener()
#
#
#    def listener(self):
#        """
#        main socket process
#        :return:
#        """
#        while True:
#            data , addr = self.socket.recvfrom(1024)
#            #self._session_handler(self._create_session_identifier(addr))
#            message = SipMessage(data)
#            #print(message)
#            if message.sip_type != None:
#                if not self.session_table.is_session(self._create_session_identifier(addr)):
#                    self.session_table.set_session(self._create_session_identifier(addr),self.application)
#                    self.session_table.session_recv(self._create_session_identifier(addr),message)
#                    print(self.session_table.session_send(self._create_session_identifier(addr)))
#
#
#
#    def register_app(self,app):
#        """
#        registers katari app to server
#        :param app:
#        :return:
#        """
#        self.application = app
#
#    def parse_sip(self,message):
#       return SipParser(message)
#
#    def _create_session_identifier(self,ip_port):
#        return ":".join([ip_port[0],str(ip_port[1])])
#
#
#    def _session_handler(self,session_identifier):
#        if self.session_table.get_session():
#            return self.session_table.get_session()
#        else:
#            self.session_table.set_session(session_identifier)
#
#    def _thread_dispatch_handler(self):
#        pass
#
#