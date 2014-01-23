import xml.etree.ElementTree as ET
import os
from FileName import *

def strCheck( string, fileName):
	if string == "teleport.wav":
		return "snd_teleport_large.wav"
	elif string == "lava.wav":
		part = fileName.getName().split('.')
		return(part[0]+".wav")
	elif string[0:4] != "snd_":
		return("snd_" + string)
	else:
		return string


def main():
	files = []
	temp  = []

	temp = os.listdir(os.getcwd())

	for f in temp:
		if os.path.isfile(f):
			f = FileName(f)
			if f.getFileExt() in '.gmx':
				files.append(f)
				#print(f.getName())

	for f in files:
		tree = ET.parse(f.getName())
		root = tree.getroot()
		orig = root.find('origname')
		strg = orig.text
		pos = 0
		for i  in range(1, len(strg)):
			if strg[-i] == '\\':
				pos = i
				break
		if pos != 0:
			strg = strg[-pos:]
		strg = strCheck(strg, f)
		orig.text = strg
		tree.write(f.getName())

if __name__ == '__main__':
	main()