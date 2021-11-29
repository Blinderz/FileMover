import shutil
from os import listdir
from os.path import isfile, join
import re


def moveFiles(sourcFolder, destinationFolder, keywords):
    sourcFolderPath = sourcFolder + "/"
    filesNames = [f for f in listdir(sourcFolderPath) if
                  isfile(join(sourcFolderPath, f))]  # take all the file's names into array
    stopCond = len(filesNames)
    if stopCond > 0:  # there are files in the folder
        for x in filesNames:
            splittedName = re.split(',| . |_|-|!|\+', x)
            if len(splittedName) >= 1:
                for key in keywords:
                    if splittedName[0] == key:   #TODO: change splittedName[0] to loop the words
                        shutil.move(sourcFolder.format(x), destinationFolder)
