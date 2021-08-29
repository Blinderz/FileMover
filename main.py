import os
import shutil

print("enter source folder's adress:")
srcFold = input()
print("enter destination folder's adress:")
dstFold = input()

shutil.move(srcFold, dstFold)
