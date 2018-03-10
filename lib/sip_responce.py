class response:
	"""
        Response Object 

        A native python object which can be queried 
        
        methods:
             parse():
                 parses sip headers from incoming sip messages 

             status():
                 will return the status-code/method from the servers message 

                   

	"""

	def __init__(self):
		self.sip_message = {}


    def parse(self,message):
    	for _lines in message.split("\n"):
    		try:
	            header,value = _lines.split(": ")
	            self.sip_message[header] = value.replace("\r","")
	        except:
	        	unknown = _lines.split(": ")
	            if "SIP/2.0" in unknown[0]:
	    	        self.sip_message["Status-Code"] = unknown[0]
	            else:
	    	        pass

	def status(self)
	    pass

