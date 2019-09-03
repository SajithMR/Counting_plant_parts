"""
These functions are indetend to use with the output json file of the annotaion tool hosted in google firebase 
"""

__author__ = 'Sajith Rajapaksa'
__version__ = '-0.1'


import random
import pandas as pd
import numpy as np
import os
import skimage.io as io
from gen_gam_image import *
import matplotlib.pyplot as plt
import urllib.request
import sys
from openFiles import *


def readJson(location, key):
    """
    read the json as a pandas dataframe 
    @param location : location of the saved json file 
    @param key : options "FLOWER","flowers","plants","plots","wheat"


    Args:
        location (TYPE): Description
        key (TYPE): Description

    Returns:
        TYPE: Description


    """
    data = pd.read_json(location)
    # removes all nan rows from the given key
    data = data[key].dropna()

    return data


# get stats

def getCountsasCSV(data, filename):
    '''
    given a pandas dataframe and a filelocation sumries the annoration data

    Args:
        data (pd dataframe): pandas dataframe containing output from readJson
        filename (string): file location to save the csv output 

    '''
    dic = {
        "plot_id": list(),
        "count": list(),
        "user_id": list(),
        "user_name": list(),
        "time": list(),
        "confidence": list(),
        "image_name": list()
    }
    print(data)
    for i in data.keys():

        dic["plot_id"].append(data[i]["plot_id"])
        dic["count"].append(len(data[i]["flowers"]))
        dic["user_id"].append(data[i]["user_id"])
        dic["user_name"].append(data[i]["user_name"])
        dic["time"].append(data[i]["end_time"] / (1000 * 60))
        dic["confidence"].append(data[i]["sub_section_confidence"])
        dic["image_name"].append(data[i]["image_name"])

    df = pd.DataFrame(dic)
    df.to_csv(filename)
    return dic


def fileTodict(file, start, end):
    """crates a dictionary using idexed file name of a given directory 

    Args:
        file (string): location of the direactory  
        start (int): start int of the index. preferably a negative index ex:abcd b = -3 
        end (int): end index, preferably in negative index 

    Returns:
        python dictornary: containg keys as the indexed str of the file name to the location of the file 
    """
    dic = {}
    names = os.listdir(file)
    for i in names:
        dic[i] = os.path.join(file , i)
        print(os.path.join(file , i))

    return dic


def getDots(data):
    """  get the locations of the annotaions from the json file 

    Args:
        data (TYPE): pandas data frame 

    Returns:
        Dictionary: plot id to 
    """
    # TODO: this is a bug fix it so multiple annotations for a image/plot can
    # be ued -lazy you
    dic = {}

    for i in data.keys():

        vertical = pd.read_json(pd.DataFrame(data[i]["flowers"]).to_json(orient='records'),
                                orient='records')
        points = np.transpose(np.array(
            [vertical["x"].values.tolist(), vertical["y"].values.tolist()]), (1, 0))
        dic[data[i]["plot_id"]] = points

    return dic


def matchDataToImagesSize(dataFile, ImageFile, crop):
    '''
    matches the id in the pandas data to the actual image 


    Args:
        dataFile (TYPE): Description
        ImageFile (TYPE): Description
        Output (TYPE): Description


    '''
    dic = {}
    data = readJson(dataFile, crop)
    data = getDots(data)

    files = fileTodict(ImageFile, 0, 4)  # start, end
    print(data.keys())

    for i in files.keys():

        print(i)
        img = io.imread(files[i])
        try:
            dic[i] = [data[i[4:8]], img.shape]
        except:
            pass
    return dic


def downloader(image_url, image_name):
    """Downloads images form a url 
    
    Arguments:
        image_url {String} --URL
        image_name {string} -- name of the image 
    """
    file_name = image_name
    full_file_name = str(file_name) + '.jpg'
    urllib.request.urlretrieve(image_url, full_file_name)


if __name__ == "__main__":
    df = readJson("/home/sajith/Downloads/floweranno-8f1b1-export.json", "flowers")
    getCountsasCSV(df,"test2.csv")