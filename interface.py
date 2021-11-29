# declarations:
from sqlparse import keywords
from fileMover import moveFiles

srcFolderPath = ""
outputFolderPath = ""
pcUsername = ""

print("Hi!")
print("Do you want to enter a input folder path or use 'Downloads' (default)?")
print("to enter a path press 1")
srcFolderSelect = input("press anything else for 'Downloads'")
if srcFolderSelect == '1' or srcFolderPath == 1:
    srcFolderPath = input("Enter a valid full path to folder")
else:
    pcUsername = input("enter your pc username")
    srcFolderPath = "C:/Users/"+pcUsername+"/Downloads"
print("chosen path is " + srcFolderPath)
outputFolderSelect = input("Do you want to enter a output folder path (1) or use 'Desktop'(2)?")
if outputFolderSelect == '1' or outputFolderPath == 1:
    outputFolderPath = input("Enter a valid full path to folder")
else:
    if pcUsername == "":
        pcUsername = input("enter your pc username")
    outputFolderPath = "C:/Users/"+pcUsername+"/Desktop"
print("how many keywords you want to search by?")
numberOfKeyWords = int(input("the keywords should will be the starting words of the category"))
keywordsList = []
for i in range(numberOfKeyWords):
    key = input("enter keyword")
    keywordsList.append(key)
moveFiles(srcFolderPath, outputFolderPath, keywordsList)
