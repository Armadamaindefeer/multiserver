#>>-----------Import----------------<<

import os
import json
import sys
import cmd
import colorama
from data.library.logging import log
from data.library.constant import *

SOURCE = __name__
SOURCE_USER = 'USER'
CMD_PREFIX = '/'

def getUserInput():
	print('>> ',end='')
	return input()


def echo(args):
	args = args.replace('echo ', '', 1)
	log(INFO , 'User', args)

def cmdHandler():
	answer = getUserInput()
	if answer[0] == '/':
		answer = answer.replace(CMD_PREFIX, '', 1)
		cmd = answer.split()
		try :
			globals()[cmd[0]](answer)
		except KeyError:
			log(ERROR, SOURCE, 'Invalid command')
