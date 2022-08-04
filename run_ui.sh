#!/bin/sh
#temp solution
sleep 30
source env/bin/activate
pytest
deactivatebackstop $1