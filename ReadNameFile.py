import shutil
from os import listdir
from os.path import isfile, join
import re

#declarations
dstFold = "C:/Users/Home/Desktop/Nanatsu No Taizai S05"
mypath = "C:/Users/Home/Downloads"
srcFold = "C:/Users/Home/Downloads/{}"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]  # take all the file name in array
stopCond = len(onlyfiles)
if(stopCond>0):   #there are files in the folder
    for x in onlyfiles:
       nameArr = re.split(',| . |_|-|!|\+', x)
       #foldName = nameArr[0]+nameArr[1]
       if (len(nameArr)>=2):
            if (nameArr[0] == "Nanatsu" or nameArr[1] == "Nanatsu"):
               shutil.move(srcFold.format(x), dstFold)
       #print(nameArr)