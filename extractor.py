import cv2

input_path = cv2.VideoCapture('videos/example_01.mp4')

def saveFrame(startSec, endSec):
    input_path.set(cv2.CAP_PROP_POS_MSEC,startSec*1000)
    hasFrames, image = input_path.read()    
    output_path = (r'C:\Users\user\Desktop\Video to frame\images')
    if hasFrames:
        cv2.imwrite(output_path + "\\frame%d.jpg" % frame_name_count, image)
    return hasFrames

fps = 1
startSec = 19
endSec = 26
count = 1
frame_name_count = 19

while saveFrame(startSec, endSec):
    count += 1
    frame_name_count += 1
    startSec += fps
    if startSec == endSec - 1:
        break

print("Extracted Images: ", count)
