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
	return open((workingDir + name), 'wb').write(r.content)

#>>-----------Main------------------<<

SOURCE = __name__



def checkLib():


	log(INFO, SOURCE, 'Starting Update Checker')
	tempManifest = getLibManifest(TEMP_DIR + '/')
	with open(LIBRARY_DIR + '/manifest.json', 'r') as m:
		manifest = json.load(m)
	log(INFO, SOURCE, 'Getting new manifest')
	changeManifest = False

	for temp in tempManifest['library']:
		countTwoLib = 0
		for old in manifest['library']:

#Update of library

			if temp['name'] == old['name']:
				if temp['version'] != old['version']:
					log(INFO, SOURCE, 'Updating library %s (%s -> %s)from %s' % (temp['name'],old['version'],temp['version'],temp['download']))
					if not downloadFiles(temp['download'], temp['name'], LIBRARY_DIR + '/'):
						log(ERROR, SOURCE,'Error while updating %s' % temp['name'])
					else:
						countTwoLib += 1
						changeManifest = True
						log(INFO, SOURCE, 'Sucessful !')
				else:
					countTwoLib += 1

#Downloading of new library

		if countTwoLib <= 0 and temp['required']:
			log(INFO, SOURCE, 'Downloading library %s from %s' % (temp['name'], temp['download']))
			if not downloadFiles(temp['download'], temp['name'], LIBRARY_DIR + '/'):
				log(ERROR, SOURCE, 'Error while downloading %s' % temp['name'])
			else:
				changeManifest = True
				log(INFO, SOURCE, 'Sucessful !')

#Downloading new launcher

	if tempManifest['launcher']['version'] != manifest['launcher']['version']:
		log(INFO, SOURCE, 'Upgrading la	launcher')
		if not downloadFiles(tempManifest['launcher']['download'], tempManifest['launcher']['name']):
				log(ERROR, SOURCE, 'Error while downloading %s' % temp['name'])
		else:
				changeManifest = True
				log(INFO, SOURCE, 'Sucessful !')

#Update Manifest if needed

	if  changeManifest:
		log(INFO, SOURCE, 'Updating manifest')
		os.replace(TEMP_DIR + '/manifest.json',  LIBRARY_DIR + '/manifest.json')
	log(INFO, SOURCE, 'Job Finish !')
