import unittest
from Katari.sip import SipMessage
from Katari.server.udp import UDPSipServer
from Katari.template import settings



sip_register = """REGISTER sip:127.0.0.1;transport=UDP SIP/2.0\n\r
Via: SIP/2.0/UDP 79.67.45.128:48189;branch=z9hG4bK-524287-1---3e839db9fc45b2cc;rport\n\r
Max-forwards: 70\n\r
Contact: <sip:43210@79.67.45.128:48189;rinstance=d3f929033197d10a;transport=UDP>\n\r
To: "sdasdasd"<sip:43210@127.0.0.1;transport=UDP>\n\r
From: "sdasdasd"<sip:43210@127.0.0.1;transport=UDP>;tag=2c8fbf43\n\r
Call-id: _LMPeTigreTCSC3D0B32zw..\n\r
Cseq: 8 REGISTER\n\r
Expires: 60\n\r
Allow: INVITE, ACK, CANCEL, BYE, NOTIFY, REFER, MESSAGE, OPTIONS, INFO, SUBSCRIBE\n\r
User-agent: Z 5.2.28 rv2.8.115\n\r
Allow-events: presence, kpml, talk\n\r
Content-length: 0\n\r
\n\r
"""



class UDPServerTesting(unittest.TestCase):

    def test_aclcorrect(self):
        UDPSipServer.settings = settings
        self.assertTrue(UDPSipServer.check_allowed("127.0.0.1"))

    def test_aclfailure(self):
        UDPSipServer.settings = settings
        self.assertFalse(UDPSipServer.check_allowed("127.0.0.2"))


class SipParsingTests(unittest.TestCase):

    def test_sip_parse(self):
        message = SipMessage(message=sip_register.encode())

        print("""sdasdasd"<sip:43210@127.0.0.1;transport=UDP>""")

        if message.get_to() == '"sdasdasd"<sip:43210@127.0.0.1;transport=UDP>':
            print("YES")
        print("NO")
        #print(type(""""sdasdasd"<sip:43210@127.0.0.1;transport=UDP>"""))
        #self.assertEqual(str(message.get_to()), """"sdasdasd"<sip:43210@127.0.0.1;transport=UDP>""")



if __name__ == '__main__':
    unittest.main()