import cv2
import numpy as np
import random

def blur_image(image):
    # Create a Gaussian blur kernel with a random kernel size
    kernel_size = random.randint(1, 21)
    kernel = (kernel_size, kernel_size)

    # Apply Gaussian blur to the image
    return cv2.GaussianBlur(image, kernel, 0)

def add_noise(image):
    # Create a noisy image by adding random values to the original image
    row, col, _ = image.shape
    mean = 0
    var = random.uniform(0, 50)
    sigma = var**0.5
    noise = np.random.normal(mean, sigma, (row, col, 3))
    noisy_image = image + noise

    # Clipping the image to keep its values between 0 and 255
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)

    return noisy_image

def add_black_spot(image):
    # Add a black spot to the image by replacing a random rectangular region with zeros
    row, col, _ = image.shape
    spot_width = random.randint(10, 50)
    spot_height = random.randint(10, 50)
    x = random.randint(0, row - spot_height)
    y = random.randint(0, col - spot_width)

    image[x:x+spot_height, y:y+spot_width] = 0

    return image

def degrade_image(image):
    # Degrade the image by applying a random combination of the blur, noise and black spot functions
    operations = [blur_image, add_noise, add_black_spot]
    operation = random.choice(operations)
    degraded_image = operation(image)

    return degraded_image

image = cv2.imread({path of image})
result_image = function_name()
filename = {os module}
cv2.imwrite(".jpg",result_image)
