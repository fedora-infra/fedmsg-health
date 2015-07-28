#!/bin/bash

python make_pages.py

cp build/*.html ~/scratch/threebean.org/.

~/.virtualenvs/awscli/bin/aws s3 sync ~/scratch/threebean.org s3://threebean.org
