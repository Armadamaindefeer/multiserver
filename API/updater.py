#>>-----------Import----------------<<

import json
import os
import requests
import sublibrary.constant

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

def downloadLib(url, name, workingDir)
	r = requests.get(url)
	if not open((workingDir + '/' + name), 'wb').write(r.content)
		return False
	else:
		return True



#>>-----------Main------------------<<

def checkLib():

	countLib = 0
	countTempLib = 0
	with open(LIBRARY_DIR + '/manifest.json', 'r') as manifest:
		libManifest = json.load(manifest)

	for key in tempLibManifest['library']:

		countTwoLib = 0
		for kex in libManifest['library']:
#Update of library
			if key['name'] == kex['name'] and key['version'] != kex['version']:
				if 'subfolder' in key and key['subfolder'] == True:
					if not downloadLib(key['download'], key['name'], SUB_LIBRARY_DIR):
						print('Error while updating')
					else:
						countTwoLib += 1
						changeManifest = True
				else:
					if not downloadLib(key['download'], key['name'], LIBRARY_DIR):
						print('Error while updating')
					else:
						countTwoLib += 1
						changeManifest = True
#Downloading of new library
		if countTwoLib <= 0 and key['required']:
			if 'subfolder' in key and key['subfolder'] == True:
				if not downloadLib(key['download'], key['name'], SUB_LIBRARY_DIR):
					print('Error while updating')
				else:
					changeManifest = True
			else:
				if not downloadLib(key['download'], key['name'], LIBRARY_DIR):
					print('Error while updating')
				else:
					changeManifest = True
	if  changeManifest:
		os.replace(TEMP_DIR + '/manifest.json',  LIBRARY_DIR + '/manifest.json')
