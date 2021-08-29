import os
import shutil

print("enter absolute file's path:")
srcFold = input()
print("enter destination folder's path:")
dstFold = input()

shutil.move(srcFold, dstFold)

