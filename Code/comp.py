import cv2
import os
import numpy as np
img_folder = r'C:\Users\Admin\Desktop\google-images-download-master\google_images_download\downloads\noise_images'
noise_folder = r'C:\Users\Admin\Desktop\google-images-download-master\google_images_download\downloads\orig_images'

list_images = os.listdir(img_folder)
list_noise = os.listdir(noise_folder)

for img in list_images:
    #for noise_path in list_noise:
    #if img == noise_path:
    frame=cv2.imread(os.path.join(img_folder,img),1)
    noise=cv2.imread(os.path.join(noise_folder, img),1)
    cv2.imshow('frame',frame)
            
    cv2.imshow('result',noise)
    key = cv2.waitKey(0)
    if key in [27,ord('q'),ord('Q')]:
        break
        exit()        
                    

            
        