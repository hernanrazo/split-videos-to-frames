import cv2
import numpy as np
import os

path_to_save = 'data/images/passenger/'

#get filepath for desired video
cap = cv2.VideoCapture('YOUR_FILE_PATH_HERE')
currentFrame = 0

while(True):

    #capture each frame
    ret, frame = cap.read()

    # Save frame as a jpg file
    name = 'frame' + str(currentFrame) + '.jpg'
    
    print ('Creating...' + name)
    cv2.imwrite(os.path.join(path_to_save, name), frame)

    #keep track of how many images you end up with
    currentFrame += 1


#release capture 
cap.release()
cv2.destroyAllWindows()

print('done')
