#!/usr/bin/env python
# stupid test script

import logpyle
import time,os,sys,random

A=sys.platform
B="string, sexy string"
counter=1
while counter<10:
  #print counter
  logpyle.logger("some other useless action", A)
  logpyle.logger("CRITICAL ERROR", B)
  logpyle.logger()
  counter += 1
  time.sleep(random.randrange(1,10))
