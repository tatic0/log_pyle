#!/usr/bin env python
# logpyle.py

# simple python logging facility

# python imports
import time, os, sys

# default values for logger
debug=False
user=os.getlogin()
program=sys.argv[0]
defaultlogfile="simple.log"
action="log line"

def logger(*action):
  #debug = True
  NOW=time.strftime('%Y/%m/%d %H:%M:%S ')
  if debug == True:
    print("debug mode on")
    print("timestap: %s user: %s program: %s action: %s") %(NOW,user,program,action)
  logging = open(defaultlogfile,'a')
  data=("%s %s %s %s\n") %(NOW,user,program,action)
  logging.write(data)
  logging.close()

