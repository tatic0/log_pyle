log_pyle
========

simple, un-complicated, "Ready To Fly" logging facility for python 

example:

import logpyle

logpyle.logger()
# outputs the default log line

OR

import logpyle
logpyle.logger(True,"other_user","custom_program","CRITICAL ERROR") 
# outputs a "custom" log line
