#!/usr/bin/env python
import lololo as logpyle
import time

# stupid test script
counter=1
while counter<10:
  #print counter
  logpyle.logger()
  logpyle.logger(user="other_user",program="custom_program",action="CRITICAL ERROR")
  counter += 1
  time.sleep(1)
