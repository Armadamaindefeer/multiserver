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

print('Downloading library')
for key in libManifest['library']:
	if key['required']:
		r = requests.get(key['download'])
		print('Downloading %s from %s' % (key['name'], key['download']))
		if 'subfolder' in key and key['subfolder'] = true:
			os.mkdir(LIBRARY_DIR + '/' + key['name'])
			if not open((LIBRARY_DIR + '/' + key['name'] + '/' + key['name']), 'wb').write(r.content):
				print('Error while downloading %s' % key['name'])
		else:
			if not open((LIBRARY_DIR + '/' + key['name']), 'wb').write(r.content):
				print('Error while downloading %s' % key['name'])
	elif not key['required']:
		print('Library %s ignored [not required]' % key['name'])
