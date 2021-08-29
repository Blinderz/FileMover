
from os import listdir
from os.path import isfile, join

mypath = "C:/Users/saarr/Desktop/projects/FileMover"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]  # take all the file name in array
print(onlyfiles[1])
