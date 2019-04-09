"""
Sip Builder class
~~~~~~~~~~~~~~~~~

builds OrderedDict and create string based off rfc 2822 syntax which sip follows
"""

from Katari.sip import SipObject
from collections import OrderedDict


class SipBuilder(SipObject):

    def __init__(self):
        self._sip_message = OrderedDict()
        self.to = None
        self.from_ = None
        self.via = None
        self.call_id = None
        self.contact = None
        self.allow = None




    def set_via(self, via):
        self.via = via

    def set_from(self, from_):
        self.from_ = from_

    def set_to(self, to):
        self.to = to

    def set_contact(self, contact):
        self.contact = contact

    def set_call_id(self, call_id):
        self.call_id = call_id

    def set_allow(self, allow):
        self.allow = allow

    def set_message_type(self, message_type):
        self.sip_type = message_type


    def tostring(self):
        pass


    def _export(self):
        pass



