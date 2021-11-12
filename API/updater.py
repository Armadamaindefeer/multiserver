#>>-----------Import----------------<<

import json
import os
import requests

#>>-----------Function--------------<<

def getNameFromGithub(url):
	if url.find('/'):
		return (url.rsplit('/', 1)[1])


def getLibManifest():
	print('Downloading manifest')
	urlManifest = 'https://raw.githubusercontent.com/Armadamaindefeer/multiserver/main/manifest.json'
	r = requests.get(urlManifest)
	manifest = open(('.intern/.temp/' + getNameFromGithub(urlManifest)), 'wb').write(r.content)

	return libManifest


def checkLib():
	tempLibManifest = getLibManifest()
	with open('.intern/.temp/manifest.json', 'r') as manifest:
		libManifest = json.load(manifest)
	countLib = 0
	countTempLib = 0
	for key in tempLibManifest['lib']:
		countTempLib += 1
		for keyb in libManifest['lib']:
			countLib += 1
			if key['name'] == keyb['name'] and key['version'] != keyb['version'] :
				r = requests.get(key['download'])
				if not open((internDir + '.lib/' + key['name']), 'wb').write(r.content):
					print('Error while updating')

	countLib = countLib/countTempLib
	if countLib != countTempLib:
		print('Error while updating')
def main():
	return 0
