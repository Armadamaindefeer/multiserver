#>>-----------Import----------------<<

import json
import sys
import os
import cmd
import requests
import colorama
import data.lib.utility
import data.lib.updater
#import data.lib.constant
from data.lib.logging import log

import keyboard
if keyboard.read_key() == "a":
    print("A Key Pressed")
