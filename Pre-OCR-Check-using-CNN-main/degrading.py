import os
import cv2
import numpy as np
import random

"""
blur
1,3 very good
5,7 good
9-11 bad
11-13 very bad

noise
0 - 0.5 very good
0.5 - 0.8 good
0.8 - 1.1 bad
beyond 1.1 very bad

spot
for good less than 0.0001
for bad between 0.0001 to 0.0002
very bad between 0.0002 to 0.0003
"""
# setting level of quality
level = 'very_bad'
# macking output directories
os.system(f'cd ./output/ && mkdir {level}')
os.system(f'cd ./output/{level}/ && mkdir _noise _blur _spot')

# setting up threshold values acc to level of quality
if level == 'very_good':
  noises =(0,0.4)
  kernals = [1,3]
  spot_factor = [0,0.0001]
elif level == 'good':
  noises = (0.4,0.7)
  kernals = [5,7]
  spot_factor = [0.0001,0.0002]
elif level == 'bad':
  noises = (0.7,0.9)
  kernals = [9,11]
  spot_factor = [0.0002,0.0003]
elif level == 'very_bad':
  noises = (0.9,1.1)
  kernals = [11,13]
  spot_factor = [0.0003,0.0005]
#############################################

# blur function
def blur_image(image):
    kernal_size = random.choice(kernals) 
    return cv2.GaussianBlur(image, (kernal_size,kernal_size), 100)

# noise function
def add_noise(image):
    # Create a noisy image by adding random values to the original image
    row, col, _ = image.shape
    mean = 0
    var = random.uniform(0, 50)
    sigma = var**(random.uniform(*noises))*(row*col//100000)
    noise = np.random.normal(mean, sigma, (row, col, 3))
    noisy_image = image + noise

    # Clipping the image to keep its values between 0 and 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    return noisy_image

# adds small black spots in image 
def add_black_spot(image):
    # Add a black spot to the image by replacing a random rectangular region with zeros
    row, col, _ = image.shape
    spot_width = random.randint(5, 10)
    spot_height = random.randint(5, 10)
    spot_density = int(row*col*(random.uniform(*spot_factor)))
    for _ in range(spot_density):
        x = random.randint(0, row - spot_height)
        y = random.randint(0, col - spot_width)
        image[x:x+spot_height, y:y+spot_width] = 0

    return image

# function to apply above filters on image
def degrade_image(image,filename,level):
    # Degrade the image by applying a random combination of the blur, noise and black spot functions
    operations = {add_noise:"_noise", add_black_spot:"_spot"}
    for operation in operations:
        result = operation(image)
        cv2.imwrite(f'./output/{level}/{operations[operation]}/'+filename+operations[operation]+".jpg",result)