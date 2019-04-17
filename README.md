# Katari - SIP (Session Initiated Protocol) Application Framework

[![PyPI pyversions](https://img.shields.io/pypi/status/Katari.svg)](https://pypi.org/project/Katari/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/Katari.svg)](https://pypi.python.org/pypi/Katari/)
[![PyPI license](https://img.shields.io/pypi/l/Katari.svg)](https://pypi.python.org/pypi/Katari/)


## installing

```

pip install Katari 

```

## An Example

```python

from Katari import KatariApplication
from Katari.sip.response._2xx import OK200

app = KatariApplication()

@app.register()
def do_register(request):
     app.send_response(request.create_response(OK200()))


app.run()

```
