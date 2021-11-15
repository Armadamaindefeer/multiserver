#>>-----------Import----------------<<

import json
import sys
import os
import cmd
import requests
import colorama

#>>-----------Function--------------<<

def createDirectory(name):
	if not os.path.isdir(name + '/'):
		os.mkdir(name)

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

def downloadFiles(url, name, workingDir=''):
	r = requests.get(url)
	return open((workingDir + name), 'wb').write(r.content)

#>>-----------Main------------------<<

DATA_DIR = 'data'
CONFIG_DIR = DATA_DIR + '/config'
LIBRARY_DIR = DATA_DIR + '/library'
TEMP_DIR = DATA_DIR + '/.temp'
SERVER_DIR = DATA_DIR + '/servers'

#Teste and create directory (data/ ; data/config/ ; data/servers ; data/.temp/ ; data/library )

print('Creating tree directory')
createDirectory(DATA_DIR)
createDirectory(CONFIG_DIR)
createDirectory(SERVER_DIR)
createDirectory(LIBRARY_DIR)
createDirectory(TEMP_DIR)

libManifest = getLibManifest(LIBRARY_DIR + '/')

for key in libManifest['library']:
	if key['required']:
		print('Downloading %s from %s' % (key['name'], key['download']))
		if not downloadFiles(key['download'], key['name'], LIBRARY_DIR + '/'):
			print('Error while downloading %s' % key['name'])
	elif not key['required']:
		print('Library %s ignored [not required]' % key['name'])
downloadFiles(libManifest['launcher']['download'], libManifest['launcher']['name'])
print('Do you want to start MultiServer now ? [Y/n]')
answer = str(input())
if answer == 'Y' or answer == 'y' or answer == 'o' or answer == 'O':
	print('Starting...')
	import MultiServer as m
	m.main()
elif answer == 'N' or answer == 'n':
	print('Stopping..')
else:
	print('Starting...')
	import MultiServer as m
	m.main()
