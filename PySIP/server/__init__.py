import SocketServer
from PySIP.sip.parser import SipParser

class SipServer(SocketServer.DatagramRequestHandler):

    def __call__(self, *args, **kwargs):
        response = self.application._server_run(self.parse_sip(args))
        self.request.sendall(response)




    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.application = None


    def handle(self):
        datagram = self.rfile.readline().strip()
        print datagram


    def start(self):
        self.listener()


    def listener(self):
        server = SocketServer.ThreadingUDPServer((self.host,self.port), self)
        server.serve_forever()


    def register_app(self,app):
        self.application = app



    def parse_sip(self,message):
       return SipParser(message[0][0])















