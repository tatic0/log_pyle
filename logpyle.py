#!/usr/bin env python
# logpyle.py
"""simple python logging facility"""

# python imports
import time
import os
import sys
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('simple.conf')
defaultlogfile = config.get('logfile', 'logfile')
action = config.get('action', 'action')


# default values for logger
debug = False
user = os.getlogin()
program = sys.argv[0]
#defaultlogfile="simple.log"
#action="log line"

def logger(*action):
  #debug = True
  current_time = time.strftime('%Y/%m/%d %H:%M:%S ')
  if debug == True:
    print("debug mode on")
    print("timestap: {} user: {} program: {} action: {}".format(current_time, user, program, action))
  logging = open(defaultlogfile, 'a')
  data = ("{} {} {} {}\n".format(current_time, user, program, action))
  logging.write(data)
  logging.close()

