import os
import xml.etree.ElementTree as ET
import sys
from FileName import *

class SoundFile(object):
    tree     = ET
    fileName = FileName
    filedir  = ""
    found    = False

    def __init__(self, fileName):
        self.fileName = fileName

    def addTree(self, tree):
        self.tree = tree
        self.root = tree.getroot()


def main():
    audioFiles = []
    audioDirs  = []
    temp       = []

    temp = os.listdir(os.getcwd())

    for f in temp:
        f = FileName(f)
        if f.getFileExt() == '.gmx':
            audioDirs.append(f)


    newDir = os.getcwd() + os.sep + 'audio'

    if os.path.isdir(newDir):
        audioFiles = os.listdir(newDir)
    else:
        print(newDir + " Does not exist program will now die")
        sys.exit()

    temp = []
    for i in audioDirs:
        temp.append(i)
    audioDirs = []

    for i in temp:
        audioDirs.append(SoundFile(i))

    for i in audioDirs:
        i.addTree(ET.parse(i.fileName.getName()))
        i.orig = i.root.find('origname')
        i.fileDir = i.orig.text

    notFound = []
    for i in audioDirs:
        found = False
        for j in audioFiles:
            if i.fileDir == j:
                found = True
        if not found:
            notFound.append(i)

    for i in notFound:
        print(i.fileName.getName())
        print(i.fileDir)
        print("===")

if __name__ == '__main__':
    main()

