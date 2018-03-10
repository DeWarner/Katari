import random

class Sessions:
    def __init__(self):
        self.current = None

    def genCall_ID(self):
        callid = random.randint(111111111111,999999999999)
        return str(callid) 

    def genTag_ID(self):
        tagid = random.randint(111111111,999999999)
        return str(tagid)
  

