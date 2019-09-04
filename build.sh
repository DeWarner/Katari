#!/bin/bash

rm dist/Katari*
pip3 uninstall Katari -y
python3 setup.py bdist_wheel
pip3 install dist/Katari*