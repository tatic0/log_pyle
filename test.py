#!/usr/bin/env python
import lololo as logpyle
import time,os,sys

A=sys.platform
B="string, sexy string"
# stupid test script
counter=1
while counter<10:
  #print counter
  logpyle.logger("some other useless action", A)
  logpyle.logger("CRITICAL ERROR", B)
  counter += 1
  time.sleep(1)
