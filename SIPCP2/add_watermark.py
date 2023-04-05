#SIPCP2
import cv2
import numpy as np
import glob
import os

logo = cv2.imread("C:/Users/rugve/SIPCP2/mylogo.png")

logoHeight, logoWidth, _ = logo.shape

images_path = glob.glob("C:/Users/rugve/SIPCP2/images/*.*")

print("Adding watermark")

for img_path in images_path:
    img = cv2.imread(img_path)
    imgHeight, imgWidth, _ = img.shape

    # Get the center of the original. It's the location where we will place the watermark
    yImgCenter = int(imgHeight / 2)
    xImgCenter = int(imgWidth / 2)
    
    top_y = yImgCenter - int(logoHeight / 2)
    left_x = xImgCenter - int(logoWidth / 2)
    bottom_y = top_y + logoHeight
    right_x = left_x + logoWidth

    # Get ROI
    ROI = img[top_y: bottom_y, left_x: right_x]

    # Add the Logo to the ROI using dst=α⋅img1+β⋅img2+γ, Blending the images together
    
    result = cv2.addWeighted(ROI, 1, logo, 0.3, 0) 

    # Replace the ROI on the image
    img[top_y: bottom_y, left_x: right_x] = result

    # Get filename and save the image
    filename = os.path.basename(img_path)
    cv2.imwrite("images/watermarked_" + filename, img)


print("Watermark added to all the images")

