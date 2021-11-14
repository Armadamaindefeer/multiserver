#>>-----------Import----------------<<

import os
import json
import sys
import cmd
import datetime
from data.library.constant import *
#format : [HH:MM:SS] [SOURCE/LEVEL]:content
# %th %tm %ts %s %l %c

#>>-----------Function--------------<<

def getLevelString(level):
	if level == DEBUG:
		return 'DEBUG'
	if level == INFO:
		return 'INFO'
	if level == WARM:
		return 'WARM'
	if level == ERROR:
		return 'ERROR'
	if level == CRITICAL:
		return 'CRITICAL'

#def storeLog():
	#placeholder

#def storeCrashLog():
	#placeholder

#>>-----------Main------------------<<

def log(level, source, content):
	now = datetime.datetime.now()
	hour = '{:02d}'.format(now.hour)
	minute = '{:02d}'.format(now.minute)
	second = '{:02d}'.format(now.second)
	format_level = getLevelString(level)

	print('[%s:%s:%s][%s/%s]%s' % (hour, minute, second, str(source), format_level, str(content)))
