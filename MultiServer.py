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

def init():
	updater.checkLib()

def main():
	running = True

	while running :
		utility.cmdHandler()



if __name__ == '__main__':
	init()
	main()
