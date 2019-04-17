"""
Holds ip and port per session
"""
import threading
import queue



class SipSessionTable:
    def __init__(self):
        self.session_table = {}
        self.application = application

    def get_session(self, session_identifier):
        try:
            return self.session_table[session_identifier]
        except:
            return False

    def set_session(self,session_identifier, blah):
        pass


    def is_session(self):
        try:
            self.session_table[session_identifier]
            return True
        except:
            return False