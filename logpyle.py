#!/usr/bin env python
# logpyle.py

# simple python logging facility

# python imports
import time, os, sys

# default values for logger
defaultuser=os.getlogin()
defaultprogram=sys.argv[0]
defaultlogfile="simple.log"

def logger(debug = False, user = defaultuser, program = defaultprogram, action = "log line"):
  #debug = True
  NOW=time.strftime('%Y/%m/%d %H:%M:%S ')
  if debug == True:
    print("debug mode on")
    print("timestap: %s user: %s program: %s action: %s") %(NOW,user,program,action)
  logging = open(defaultlogfile,'a')
  data=("%s %s %s %s\n") %(NOW,user,program,action)
  logging.write(data)
  logging.close()

