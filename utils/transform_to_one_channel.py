import cv2
import os

#declare base path
base_path = '../data/images'
destination_path = '../data/gray_scale/images'


#get images in image directory
image_files = os.listdir('../data/images')
print(len(image_files))

for image in image_files:
    #read image 
    print(f'{base_path}/{image}')
    img = cv2.imread(f'{base_path}/{image}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f'{destination_path}/{image}')
    cv2.imwrite(f'{destination_path}/{image}',gray)
    print('[INFO] Saved!')
    
print('[INFO] Done')
    
