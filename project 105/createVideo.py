import os
import cv2 
path="Images/"

if ext in ['.gif', '.png', '.jpg','.jfif']:
    file_name=path+"/"+file_name
    print(file_name)
    size=(width,height)
    print(size)
     
     out= cv2.videoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
    
    print("done")