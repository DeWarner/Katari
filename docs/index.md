# Katari - SIP (Session Initiated Protocol) Application Framework

[![PyPI pyversions](https://img.shields.io/pypi/status/Katari.svg)](https://pypi.org/project/Katari/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/Katari.svg)](https://pypi.python.org/pypi/Katari/)
[![PyPI license](https://img.shields.io/pypi/l/Katari.svg)](https://pypi.python.org/pypi/Katari/)
![PyPI version shields.io](https://img.shields.io/pypi/dm/Katari.svg)


## Installing

```
pip install Katari 
```

## Installing from Git

```
pip install git+https://github.com/hyperioxx/Katari.git
```


## Getting Started

to create a katari project run the following command in your terminal

```bash
katari --build-app <project name>
```


#### app.py
```python
import settings
from Katari import KatariApplication
from Katari.sip.response import ResponseFactory

app = KatariApplication(settings=settings)

@app.invite()
def do_invite(request, client):
    # add INVITE logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

@app.register()
def do_register(request, client):
    # add REGISTER logic here 
    response = ResponseFactory.build(401) # 401 unauthorized 
    app.send(request.create_response(OK200()), client)

@app.options()
def do_options(request, client):
    # add OPTIONS logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

@app.info()
def do_info(request, client):
    # add INFO logic here 
    response = ResponseFactory.build(200) # 200 OK
    app.send(request.create_response(response), client)

if __name__ == "__main__":   
    app.run()

```


## Writing your own middleware

create a directory called middleware within your project

```
myproject -
   - app.py
   - settings.py
   - middleware   << LIKE THIS 
     - __init__.py
     - test.py
```

your middleware can modify the sip message before it reaches your main logic using the process_request method and also modify the response before it gets sent back to the client using process response method.

#### Example

test.py
```python 


from Katari.interfaces import MiddlewareInterface

class Test(MiddlewareInterface):
    
    def process_request(self, message):
        print(str(message))
        return message

    
    def process_response(self, message):
        print(str(message))
        return message

```

settings.py
```python
"""
##    ##    ###    ########    ###    ########  ####
##   ##    ## ##      ##      ## ##   ##     ##  ##
##  ##    ##   ##     ##     ##   ##  ##     ##  ##
#####    ##     ##    ##    ##     ## ########   ##
##  ##   #########    ##    ######### ##   ##    ##
##   ##  ##     ##    ##    ##     ## ##    ##   ##
##    ## ##     ##    ##    ##     ## ##     ## ####

SIP (Session Initiated Protocol) Application Framework

"""

HOST = "127.0.0.1" #Specify interface to listen on 

PORT = 5060 # Specify port to listen on

ALLOWED_HOSTS = ["127.0.0.1"] # Katari whitelist

USER_AGENT = "Katari Server 0.0.6" # User Agent sent in response 

# Logging settings
KATARI_LOGGING = {
                   "LOGFILE" :"Katari.log",
                   "LEVEL": "INFO", 
                   "OUTPUTMODE": "file"
                 }

# Katari middleware 
KATARI_MIDDLEWARE = [
    'middleware.test',   # Add import path here
    
]



```



# Katari API


## SIP Message Methods

```python

Katari.sip.SipMessage 
```

###Getters

#### get_to()
Returns the SIP URI within the 'To:' Header 
```python

SipMessage.get_to()
 ```

#### get_from()
Returns the SIP URI within the 'From:' Header 
```python

SipMessage.get_from()
 ```

#### get_via()
Returns the SIP URI within the 'Via:' Header 
```python

SipMessage.get_via()
 ```

#### get_contact()
Returns the SIP URI within the 'Contact:' Header 
```python

SipMessage.get_contact()
 ```

#### get_call_id()
Returns the Call Id within the 'Call-Id:' Header 
```python

SipMessage.get_call_id()
 ```

#### get_allow()
Returns the Allowed Methods within the 'Allow:' Header 
```python

SipMessage.get_allow()
 ```

#### get_cseq()
Returns the Call Sequence within the 'CSeq:' Header 
```python

SipMessage.get_cseq()
 ```

#### get_message_type()
Returns the Method/Status Code from the top line in the message 
```python

SipMessage.get_message_type()
 ```

### Setters

#### set_to()
Sets the SIP URI within the 'To:' Header 
```python

SipMessage.get_to()
```

#### set_from()
Sets the SIP URI within the 'From:' Header 
```python

SipMessage.get_from()
```

#### set_via()
Sets the SIP URI within the 'Via:' Header 
```python

SipMessage.get_via()
 ```

#### set_contact()
Sets the SIP URI within the 'Contact:' Header 
```python
SipMessage.get_contact()
 ```

#### set_call_id()
Sets the Call Id within the 'Call-Id:' Header 
```python

SipMessage.get_call_id()
 ```

#### set_allow()
Sets the Allowed Methods within the 'Allow:' Header 
```python

SipMessage.get_allow()
```

#### set_cseq()
Sets the Call Sequence within the 'CSeq:' Header 
```python

SipMessage.get_cseq()
 ```

#### set_message_type()
Sets the Method/Status Code from the top line in the message 
```python

SipMessage.get_message_type()
 ```

