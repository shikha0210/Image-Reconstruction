import cv2
import numpy as np
import os
from skimage.util import random_noise
 
# Load the image
img_folder = r'C:\Users\User\Desktop\Image reconstruction\images_148'
fn=r'C:\Users\User\Desktop\Image reconstruction\noise_images\noise_images'
list_images = os.listdir(img_folder)
list_noise = os.listdir(fn)
frameNo=592
for img in list_images:
    im=cv2.imread(os.path.join(img_folder,img))
    frameNo  += 1
# Add gaussian noise to the image.
    noise_img = random_noise(im, mode='salt')
 
# The above function returns a floating-point image
# on the range [0, 1], thus we changed it to 'uint8'
# and from [0,255]
    noise_img = np.array(255*noise_img, dtype = 'uint8')
    #cv2.imshow('blur',noise_img)
    img_name = 'salt'+'_'+str(frameNo)
    img_loc = fn+"\\"+img_name+'.jpg'
    cv2.imwrite(img_loc,noise_img)
    cv2.waitKey(0)
  
# Display the noise image
    
   
    
