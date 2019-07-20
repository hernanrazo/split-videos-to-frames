import cv2
import numpy as np
import os


#get file path for desired video and where to save frames locally
cap = cv2.VideoCapture('YOUR_FILE_PATH_HERE')
path_to_save = 'YOUR_FILE_PATH_HERE'

current_frame = 0

while(True):

    #capture each frame
    ret, frame = cap.read()

    # Save frame as a jpg file
    name = 'frame' + str(current_frame) + '.jpg'
    
    print ('Creating: ' + name)
    cv2.imwrite(os.path.join(path_to_save, name), frame)

    #keep track of how many images you end up with
    current_frame += 1
    
    #stop loop when video ends
    if not ret:
        break


#release capture 
cap.release()
cv2.destroyAllWindows()

print('done')
