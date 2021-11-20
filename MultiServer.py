#>>-----------Import----------------<<

import json
import sys
import os
import cmd
import requests
import colorama
import data.library.utility as utility
import data.library.updater as updater
from data.library.constant import *
from data.library.logging import log

SOURCE = __name__

def init():
	updater.checkLib()

def main():
	try:
		running = True
		while running :
			utility.cmdHandler()
	except KeyboardInterrupt:
		log(WARM, SOURCE, 'Soft interrupt : Do you want to exit ? [Y/n]')
		if utility.userAnswerHandler(input(), True):
			log(INFO, SOURCE, 'Stopping')
			sys.exit()

if __name__ == '__main__':
	init()
	main()
