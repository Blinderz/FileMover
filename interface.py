# declarations:
import inflect
from fileMover import moveFiles


def verifyInputType(inputType, message):
    if message is not None:
        userInput = input(message)
    else:
        userInput = input()
    if inputType == int:
        if userInput.isnumeric():
            userInput = int(userInput)
        while not (isinstance(userInput, inputType)):
            userInput = input("you have entered wrong input type, please enter a valid input of type: " + str(inputType))
            if userInput.isnumeric():
                userInput = int(userInput)
    else:
        while userInput.isnumeric():
            userInput = input("you have entered wrong input type, please enter a valid input of type: " + str(inputType))
    return userInput


wordsEngine = inflect.engine()
srcFolderPath = ""
outputFolderPath = ""
pcUsername = ""

print("Hi!")
print("Do you want to enter a input folder path or use 'Downloads' (default)?")
print("press 1 to enter a path")
print("press anything else for 'Downloads'")
srcFolderSelect = input()
if srcFolderSelect == '1' or srcFolderPath == 1:
    srcFolderPath = verifyInputType(str, "Enter a valid full path to folder")
else:
    pcUsername = verifyInputType(str, "enter your pc username")
    srcFolderPath = "C://Users//" + pcUsername + "//Downloads"
print("chosen path is " + srcFolderPath)
print("Do you want to enter a output folder path or use 'Desktop' (default)?")
print("press 1 to enter a path")
print("press anything else for 'Desktop'")
outputFolderSelect = input()
if outputFolderSelect == '1' or outputFolderPath == 1:
    outputFolderPath = verifyInputType(str, "Enter a valid full path to folder")
else:
    if pcUsername == "":
        pcUsername = verifyInputType(str, "enter your pc username")
    outputFolderPath = "C://Users//" + pcUsername + "//Desktop"
print("chosen path is " + outputFolderPath)
numberOfCategories = int(verifyInputType(int, "how many categories to divide by?"))
for i in range(numberOfCategories):
    print("please name category number " + wordsEngine.number_to_words(i+1))
    categoryName = verifyInputType(str, "enter desired folder name")
    print("how many keywords you want to search by?")
    numberOfKeyWords = int(verifyInputType(int, "the keywords should be the starting words of the category"))
    keywordsList = []
    for j in range(numberOfKeyWords):
        key = verifyInputType(str, "enter keyword")
        keywordsList.append(key)
    moveFiles(srcFolderPath, outputFolderPath + "//" + categoryName, keywordsList)
