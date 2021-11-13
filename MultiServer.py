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

def main():
	updater.checkLib()


if __name__ == '__main__':
	main()
