'''
Automate script to rename files in a folder
'''

from os import listdir
import os
names = [f for f in listdir(".") if "sample-" in f]
for name in names:
    os.rename(name,name.replace("sample-","sample"))

