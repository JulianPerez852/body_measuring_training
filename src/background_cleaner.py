import pixellib
from pixellib.tune_bg import alter_bg
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image,ImageOps
from IPython.display import Image as img
from pylab import rcParams
import os


def clean_background(root_path,input_path,output_path):
    """
        Function that execute the remove background process
        this convert the backgroung pixels in 255,255,255

        root_path(os.path): root path of the proyect
        input_path(str): place where are store the images to process
        output_path(str): place where will be store the processed images
    """

    path_model=os.path.join(root_path,"pre_trained_models","xception_pascalvoc.pb") 
    path_input=os.path.join(root_path,input_path)
    path_output=os.path.join(root_path,output_path)

    rcParams['figure.figsize'] = 10, 10

    change_bg = alter_bg()

    change_bg = alter_bg(model_type="pb")

    change_bg.load_pascalvoc_model(path_model)

    list_files=os.listdir(path_input)

    for file in list_files:
        
        image_in=os.path.join(path_input,file)
        print(image_in)
        if file.__contains__("jfif"):
            file=file.replace("jfif","jpg")

        image_out=os.path.join(path_output,file)
        print(image_out)
        change_bg.color_bg(image_in, 
                   colors = (255, 255, 255), 
                   output_image_name= image_out)

    pass