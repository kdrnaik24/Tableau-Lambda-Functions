#!/bin/sh
cd lib/python2.7/site-packages
zip -q -r9 ../../../lambda.zip *
cd ../../..
zip -q -g lambda.zip lambda.py
