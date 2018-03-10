import hashlib
class sip_digest:

	def __init__(self):
		pass
    
    def Digest_Gen(self,username,password,realm,method,bwnonce,cnonce,uri):
         count = "00000001"
         auth = "auth"
         ha1 = hashlib.md5(""+username+":"+realm+":"+password+"").hexdigest()
         ha2 = hashlib.md5('%s:%s'%(method,uri)).hexdigest()
         responce = hashlib.md5("%s:%s:%s:%s:%s:%s"%(ha1,bwnonce,count,cnonce,auth,ha2)).hexdigest()
         return responce

     
