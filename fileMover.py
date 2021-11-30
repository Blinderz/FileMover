import os
import shutil
from os import listdir
from os.path import isfile, join
import re


def moveFiles(sourceFolder, destinationFolder, keywords):
    sourceFolderPath = sourceFolder  # + "/"
    #destinationFolder = destinationFolder + "/"
    filesNames = getFilesNames(sourceFolderPath)
    stopCond = len(filesNames)
    if stopCond > 0:  # there are files in the folder
        for x in filesNames:
            splitName = re.split(r"[\b\W\b]+", x)   #TODO: divide by undercore as well
            if len(splitName) >= 1:
                for key in keywords:
                    for word in splitName:
                        if word == key:
                            try:
                                if os.path.exists(destinationFolder + format(x)):
                                    print("file already exists at destination folder")
                                else:
                                    #shutil.move(sourceFolder.format(x), destinationFolder)
                                    os.replace(sourceFolder.format(x), destinationFolder.format(x))
                                    print(format(x) + "has been moved to " + destinationFolder)
                            except FileNotFoundError:
                                print(format(x) + " was not found at source folder")
                            break


# take all the file's names into array
def getFilesNames(srcPath):
    filesNames = [f for f in listdir(srcPath) if isfile(join(srcPath, f))]
    return filesNames
