import os
import json
from src.background_cleaner import clean_background

with open('config.json','r') as f:
    config = json.load(f) 

root_path=os.getcwd()



def go():

    if config["run"]["background_cleaner.py"]:

        clean_background(root_path,input_path=config["data_front"],output_path=config["output_front"])
        clean_background(root_path,input_path=config["data_side"],output_path=config["output_side"])



if __name__ == "__main__":
    go()
