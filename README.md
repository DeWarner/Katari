![alt text](https://github.com/hyperioxx/Katari/blob/master/Katari.png "Katari Logo")

# Katari - SIP (Session Initiated Protocol) Application Framework

[![PyPI pyversions](https://img.shields.io/pypi/status/Katari.svg)](https://pypi.org/project/Katari/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/Katari.svg)](https://pypi.python.org/pypi/Katari/)
[![PyPI license](https://img.shields.io/pypi/l/Katari.svg)](https://pypi.python.org/pypi/Katari/)
![PyPI version shields.io](https://img.shields.io/pypi/dm/Katari.svg)


## Documentation 

https://katari.readthedocs.io/en/latest/


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








