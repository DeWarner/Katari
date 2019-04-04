import os
from setuptools import setup,find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PySIP",
    version = "0.0.1",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("A SIP(Session Initiation Protocol) parsing library"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/PySIP",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
    ],
)