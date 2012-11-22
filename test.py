import logpyle, time

# stupid test script
counter=1
while counter<10:
  #print counter
  logpyle.logger()
  counter += 1
  time.sleep(1)
