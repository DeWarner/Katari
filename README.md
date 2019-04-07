# PySIP - Python SIP (Session Initiated Protocol) Application Framework

## installing

```
python setup.py bdist_wheel

pip install dist/PySIP-0.0.1-py2-none-any.whl

```

## An Example

```python

from PySIP import SipApplication

app = SipApplication()

app.run()

```