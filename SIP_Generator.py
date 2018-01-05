
import random
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

    headers = ["Via: SIP/2.0/","Max-Forwards: ","To: ","From: ","Call-ID: ","CSeq: ","Contact: ","Authorization: " ,"User-Agent: ","Content-Type: ","Content-Length: "]
          
    @staticmethod
    def GenerateSipMessage(method,lineport,protocol,to,displayname,proxy,Content_type,Content_length,callId=random.randint(111111111111,999999999999),cseq=1,authorization=0):
        """ Pass in UA and Call information and a SIP Message is generated """
        print method + "\r"
        for header in SIP_Generator.headers:
            if header == "Via: SIP/2.0/"+protocol+" "+proxy:
                print header 
            elif header == "Max-Forwards: ":
                print header + "70"
            elif header == "To: ":
            	recipient = "<sip:{}>".format(to)
                print header+recipient
            elif header == "From: ":
                fromLineport = "<sip:{}>".format(lineport)
                print header+displayname+" "+fromLineport+";"
            elif header == "Call-ID: ":
                print header + str(callId)
            elif header == "CSeq: ":
                print header + str(cseq) +" "+method
            elif header == "Contact: ":
            	contactLineport = "<sip:{}>".format(lineport)
                print header + contactLineport
            elif header == "Authorization: " and authorization != 0:
            	print header +" "+ """Digest username="{}", realm="{}", nonce="{}", uri="sip:{}", response="{}", algorithm=MD5, cnonce="{}", qop=auth, nc={}""".format()
            elif header == "Content-Type: ":
                print header +" "+Content_type
            elif header == "Content-Length: ":
                print header+" "+Content_length
        print "\r\r\r"
    
    

SIP_Generator.GenerateSipMessage("INVITE","test1@proxy1.co.uk","UDP","test2@proxy2.co.uk","Aaron","1.1.1.1","application/sdp","100",)


