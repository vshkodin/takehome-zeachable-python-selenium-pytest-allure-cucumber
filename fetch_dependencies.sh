#!/bin/bash

if [ -d "env" ]
then
    echo "Virtual env exists."
    source env/bin/activate
    pip install -r requirements.txt
    deactivate
else
    python3 -m pip install virtualenv
    python3 -m virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    deactivate
fi