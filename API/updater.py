#>>-----------Import----------------<<

import json
import os
import requests
from data.library.logging import log
from data.library.constant import *
#>>-----------Function--------------<<

def getNameFromGithub(url):
	if url.find('/'):
		return (url.rsplit('/', 1)[1])


def getLibManifest(workingDir):
	urlManifest = 'https://raw.githubusercontent.com/Armadamaindefeer/multiserver/main/manifest.json'
	log(INFO, SOURCE, 'Downloading manifest from %s' % urlManifest)
	r = requests.get(urlManifest)
	manifest = open((workingDir + getNameFromGithub(urlManifest)), 'wb').write(r.content)
	with open(workingDir + getNameFromGithub(urlManifest), 'r') as manifest:
		libManifest = json.load(manifest)
	return libManifest

def downloadFiles(url, name, workingDir=''):
	r = requests.get(url)
	if not open((workingDir + name), 'wb').write(r.content):
		return False
	else:
		return True



#>>-----------Main------------------<<

SOURCE = __name__



def checkLib():

	log(INFO, SOURCE, 'Starting Update Checker')
	tempManifest = getLibManifest(TEMP_DIR + '/')
	with open(LIBRARY_DIR + '/manifest.json', 'r') as m:
		manifest = json.load(m)
	log(INFO, SOURCE, 'Getting new manifest')
	changeManifest = False
	for key in tempManifest['library']:
		countTwoLib = 0
		for kex in manifest['library']:
#Update of library
			if key['name'] == kex['name']:
				if key['version'] != kex['version']:
					log(INFO, SOURCE, 'Updating library %s (%s -> %s)from %s' % (key['name'],kex['version'],key['version'],key['download']))
					if not downloadFiles(key['download'], key['name'], LIBRARY_DIR + '/'):
						log(ERROR, SOURCE,'Error while updating %s' % key['name'])
					else:
						countTwoLib += 1
						changeManifest = True
						log(INFO, SOURCE, 'Sucessful !')
				else:
					countTwoLib += 1
#Downloading of new library
		if countTwoLib <= 0 and key['required']:
			log(INFO, SOURCE, 'Downloading library %s from %s' % (key['name'], key['download']))
			if not downloadFiles(key['download'], key['name'], LIBRARY_DIR + '/'):
				log(ERROR, SOURCE, 'Error while downloading %s' % key['name'])
			else:
				changeManifest = True
				log(INFO, SOURCE, 'Sucessful !')

#Downloading new launcher
	if tempManifest['launcher']['version'] != manifest['launcher']['version']:
		log(INFO, SOURCE, 'Upgrading la	launcher')
		if not downloadFiles(tempManifest['launcher']['download'], tempManifest['launcher']['name']):
				log(ERROR, SOURCE, 'Error while downloading %s' % key['name'])
			else:
				changeManifest = True
				log(INFO, SOURCE, 'Sucessful !')

	if  changeManifest:
		log(INFO, SOURCE, 'Updating manifest')
		os.replace(TEMP_DIR + '/manifest.json',  LIBRARY_DIR + '/manifest.json')
	log(INFO, SOURCE, 'Job Finish !')
