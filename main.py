import os
import numpy as np
import argparse
import cv2

def main():

    # parse all args
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='Path to source video')
    parser.add_argument('dest_folder', type=str, help='Path to destination folder')
    args = parser.parse_args()

    # get file path for desired video and where to save frames locally
    cap = cv2.VideoCapture(args.source)
    path_to_save = os.path.abspath(args.dest_folder)
    
    current_frame = 1

    if (cap.isOpened() == False):
        print('Cap is not open')

    # cap opened successful
    while(cap.isOpened()):

        # capture each frame
        ret, frame = cap.read()
        if(ret == True):

            # Save frame as a jpg file
            name = 'frame' + str(current_frame) + '.jpg'
            print (f'Creating: {name}')
            cv2.imwrite(os.path.join(path_to_save, name), frame)

            # keep track of how many images you end up with
            current_frame += 1
        
        else:
            break

    # release capture 
    cap.release()
    print('done')

if __name__ == '__main__':
    main()
