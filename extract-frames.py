'''
Script to extract frames out of video file and save as JPEG images
'''

import cv2
print(cv2.__version__)

def extractImages(pathIn, pathOut):
    vidcap = cv2.VideoCapture(pathIn)
    count = 0
    success = True
    while success:
      success,image = vidcap.read()
      print ('Extracting frame: ', count)
      # Save frame as JPEG file
      cv2.imwrite( pathOut + "frame%d.jpg" % count, image) 
      count += 1

if __name__=="__main__":
    print("starting")
    input = "output.avi"
    # Create dir called output
    output = "output/"
    extractImages(input, output)
