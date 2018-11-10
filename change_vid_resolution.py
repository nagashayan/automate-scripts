#supports one level of directory structure
from os import listdir
from subprocess import call
import os

directories = [f for f in listdir(".")]
for name in directories:
    if ".DS_Store" not in name and not os.path.isfile(name):
            change_resolution(name)
            os.chdir("..")
def change_resolution(path):
    os.chdir(path)
    files = [f for f in listdir(".")]
    for name in files:
        if ".DS_Store" not in name and os.path.isfile(name):
            call(["ffmpeg","-i",name, "-vf", "scale=1280:960", "output/"+name, "-hide_banner"])



    
