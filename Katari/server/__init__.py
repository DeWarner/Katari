import socket
import threading
from Katari.sip import SipMessage
from Katari.server.session import SipSessionTable


class SipServer:


    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.application = None
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host,self.port))
        self.session_table = SipSessionTable()


    def start(self):
        """
        Starts the listener method
        :return:
        """
        self.listener()


    def listener(self):
        """
        main socket process
        :return:
        """
        while True:
            data , addr = self.socket.recvfrom(1024)
            self._session_handler(self._create_session_identifier(addr))
            message = SipMessage(data[0])
            if message.sip_type != None:
                if not self.session_table.is_session():
                    #


                response = self.application._server_run(message)
                self.socket.sendto(response.export().encode(),data[1])


    def register_app(self,app):
        """
        registers katari app to server
        :param app:
        :return:
        """
        self.application = app

    def parse_sip(self,message):
       return SipParser(message)

    def _create_session_identifier(self,ip_port):
        return ":".join(ip_port)


    def _session_handler(self,session_identifier):
        if self.session_table.get_session():
            return self.session_table.get_session()
        else:
            self.session_table.set_session(session_identifier)

























