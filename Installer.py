#>>-----------Import----------------<<

import json
import sys
import os
import cmd
import requests
import colorama

#>>-----------Function--------------<<

def getNameFromGithub(url):
	if url.find('/'):
		return (url.rsplit('/', 1)[1])

def getLibManifest(workingDir):
	print('Downloading manifest')
	urlManifest = 'https://raw.githubusercontent.com/Armadamaindefeer/multiserver/main/manifest.json'
	r = requests.get(urlManifest)
	manifest = open((workingDir + getNameFromGithub(urlManifest)), 'wb').write(r.content)
	with open(workingDir + getNameFromGithub(urlManifest), 'r') as manifest:
		libManifest = json.load(manifest)
	return libManifest

def downloadLib(url, name, workingDir=''):
	r = requests.get(url)
	if not open((workingDir + name), 'wb').write(r.content):
		return False
	else:
		return True

#>>-----------Main------------------<<

DATA_DIR = 'data'
CONFIG_DIR = DATA_DIR + '/config'
LIBRARY_DIR = DATA_DIR + '/library'
TEMP_DIR = DATA_DIR + '/.temp'
SERVER_DIR = DATA_DIR + '/servers'

#Teste and create directory (data/ ; data/config/ ; data/servers ; data/.temp/ ; data/library )
if not os.path.isdir(DATA_DIR):
	print('Creating tree directory')
	os.mkdir(DATA_DIR)
if not os.path.isdir(CONFIG_DIR + '/'):
	os.mkdir(CONFIG_DIR)
if not os.path.isdir(SERVER_DIR + '/'):
	os.mkdir(SERVER_DIR)
if not os.path.isdir(LIBRARY_DIR + '/'):
	os.mkdir(LIBRARY_DIR)
if not os.path.isdir(TEMP_DIR + '/'):
	os.mkdir(TEMP_DIR)

libManifest = getLibManifest(LIBRARY_DIR + '/')

for key in libManifest['library']:
	if key['required']:
		print('Downloading %s from %s' % (key['name'], key['download']))
		if not downloadLib(key['download'], key['name'], LIBRARY_DIR + '/'):
			print('Error while downloading %s' % key['name'])
	elif not key['required']:
		print('Library %s ignored [not required]' % key['name'])
downloadLib(libManifest['executor']['download'], libManifest['executor']['name'])
