#!/usr/bin/env python3
import cgi
import os
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
# look at environment variables
print(os.environ)
