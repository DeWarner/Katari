"""

      INVITE sip:bob@biloxi.com SIP/2.0
      Via: SIP/2.0/UDP pc33.atlanta.com;branch=z9hG4bK776asdhds
      Max-Forwards: 70
      To: Bob <sip:bob@biloxi.com>
      From: Alice <sip:alice@atlanta.com>;tag=1928301774
      Call-ID: a84b4c76e66710@pc33.atlanta.com
      CSeq: 314159 INVITE
      Contact: <sip:alice@pc33.atlanta.com>
      Content-Type: application/sdp
      Content-Length: 142


"""
class SIP_Generator:

    headers = ["Via: SIP/2.0/UDP","Max-Forwards:","To:","From:","Call-ID:","CSeq:","Contact:","Content-Type:","Content-Length:"]
          
    @staticmethod
    def SetUserInfo():
        pass
  

    @staticmethod
    def GenerateSipMessage(method):
        print method + "\r"
        for header in SIP_Generator.headers:
            if header == "Via: SIP/2.0/UDP":
                print header
            elif header == "Max-Forwards:":
                print header
            elif header == "To:":
                print header
            elif header == "From:":
                print header
            elif header == "Call-ID:":
                print header
            elif header == "CSeq:":
                print header
            elif header == "Contact:":
                print header
            elif header == "Content-Type:":
                print header
            elif header == "Content-Length:":
                print header
        print "\r\r\r"
    
    

SIP_Generator.GenerateSipMessage("INVITE")


