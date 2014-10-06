#!/bin/bash

python make_pages.py
scp build/*.html threebean.org:~/webapps/static/.
