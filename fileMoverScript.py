import shutil
from os import listdir
from os.path import isfile, join
import re


#replace the * with your pc username
dstFold = "C:/Users/*/Downloads"
mypath = "C:/Users/*/Downloads/"
srcFold = "C:/Users/*/Desktop"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]  # take all the file name in array
stopCond = len(onlyfiles)
if(stopCond>0):   #there are files in the folder
    for x in onlyfiles:
       nameArr = re.split(',| . |_|-|!|\+', x)
       if (len(nameArr)>=2):
            if (nameArr[0] == "one" or nameArr[1] == "Nanatsu"):    #replace 'Nanatsu' & 'One' with your search keywords
               shutil.move(srcFold.format(x), dstFold)
