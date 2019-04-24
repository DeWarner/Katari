import threading
import socketserver
from Katari.sip import SipMessage


class UDPSipServer(socketserver.DatagramRequestHandler):

    application = None


    def handle(self):
        """

        :return:
        """
        datagram = self.rfile.read()
        message = SipMessage(datagram)
        UDPSipServer.application.socket = self.request
        UDPSipServer.application.client = self.client_address
        UDPSipServer.application._server_run(message , self.client_address)


    @staticmethod
    def start(ServerAddress, applcation):
        """
        Forks application to handle request

        :param ServerAddress:
        :param applcation:
        :return:
        """
        UDPSipServer.application = applcation
        UDPServerObject = socketserver.ForkingUDPServer(ServerAddress, UDPSipServer)
        UDPServerObject.serve_forever()
