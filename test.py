#!/usr/bin/env python
import logpyle, time

# stupid test script
counter=1
while counter<10:
  #print counter
  logpyle.logger()
  logpyle.logger(True,"other_user","custom_program","CRITICAL ERROR")
  counter += 1
  time.sleep(1)
