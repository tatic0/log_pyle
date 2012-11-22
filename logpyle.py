#!/usr/bin env python
# logpyle.py

# simple python logging facility

# python imports
import time, os, sys

# default values for logger
#debug=False
defaultuser=os.getlogin()
defaultprogram=sys.argv[0]
defaultlogfile="simple.log"

def logger(debug = False, user = defaultuser, program = defaultprogram, logfile = defaultlogfile):
  NOW=time.strftime('%Y/%m/%d %H:%M:%S ')
  if debug == True:
    print("debug mode on")
  print("timestap: %s, user: %s, program: %s") %(NOW,user,program)
  logging = open(logfile,'a')
  data=("%s %s %s \n") %(NOW,user,program)
  logging.write(data)
  logging.close()

