import os
from setuptools import setup,find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Katari",
    version = "0.0.2",
    author = "Aaron Parfitt",
    author_email = "aaronparfitt123@gmail.com",
    description = ("A SIP(Session Initiation Protocol) Application Framework"),
    license = "BSD",
    keywords = "voip",
    url = "http://packages.python.org/Katari",
    packages=find_packages(),
    long_description=read('README.md'),
    scripts=['scripts/katari'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
)