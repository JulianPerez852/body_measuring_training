import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageOps
import numpy as np

def resize_image(image_route, limit_size):
    """
    
    """
    image = Image.open(image_route)

    width, height = image.size

    if height > limit_size:
        image_resize = image.resize(
            int(width*0.3),
            int(height*0.3)
            )

        new_image_array = np.array(image_resize)
        image = image_resize
    
    else:
        new_image_array = np.array(image)

    return new_image_array, image

def remove_noise(image_array):
    """
    
    """
    shapes = image_array.shape

    processement_array = np.zeros(
        (
            shapes[0],
            shapes[1],
            3
            )
        )

    pos_y = 0
    pos_x = 0

    for points in image_array:
        for R,G,B in points:
            if (R<20 and G>25 and B<20) or \
                (R<5 and G<30 and B<5) or \
                (R>20 and G<10 and B>20):
                for i in range(2):
                    processement_array[pos_y][pos_x][i] = 255
            
            else:
                for i in range(2):
                    processement_array[pos_y][pos_x][i] = image_array[pos_y][pos_x][i]
                pass

            pos_x += 1
        
        pos_x = 0
        pos_y += 1

    return processement_array

def remove_noise_refactor(image):
    """
    """
    width, height,  = image.size

    for i in range(width):
        for j in range(height):
            data = image.getpixel((i,j))
     
            if (data[0]<20 and data[1]>25 and data[2]<20) or \
                (data[0]<5 and data[1]<30 and data[2]<5) or \
                (data[0]>20 and data[1]<10 and data[2]>20):

                image.putpixel((i,j),(255, 255, 255))

    return image

def get_squeared_image(image):

    width = image.width
    height = image.height

    if height > width:

        diff = height - width

        widht_n = width + diff
        size = (widht_n, height)

        new_image = Image.new(mode = 'RGB', size= (size), color = (255,255,255))
        new_image.paste(image, (int(diff/2), 0))

    else:

        diff = width - height

        height_n = height + diff
        size = (width, height_n)

        new_image = Image.new(mode = 'RGB', size= (size), color = (255,255,255))
        new_image.paste(image, (0, int(diff/2)))

    return new_image
    
if'__main__' == __name__:
    pass