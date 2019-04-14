from Katari.sip import SipMessage


class ParsedMessage:
    def __init__(message):
        self.message = message
        self.info = parse(message)


def parse(sip_message):
    """
    Takes in a sip message
    
    :param sip_message:
    :return: dict

    >>> a = parse("<sip:cal3254@192.234.1.12:5060;transport=udp>")
    >>> a.port == 5060
    true
    >>> a.address == "cal3254@192.234.1.12"
    true
    >>> a.transport == "udp"
    true
    """
    message = sip_message[5:-1]
    # cal3254@192.234.1.12:5060;transport=udp
    if sip_message[:5] != "<sip:":
        raise Exception("tis not a sip message? :(")
    loc, tp = message.split(";")
    transport = tp.split("=")[1]
    address, port = loc.split(":")
    return dict(address=address, port=port, transport=transport)
















