import sys
import argparse

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print ('Extracting frame: ', count)
      cv2.imwrite( pathOut + "frame%d.jpg" % count, image)     # save frame as JPEG file
      count += 1

if __name__=="__main__":
    print("starting")
    
    input = "/Users/nagashayanaramamurthy/output.avi"
    output = "/Users/nagashayanaramamurthy/output/"

    extractImages(input, output)
