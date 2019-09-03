from openFiles import *
import os
import skimage.io as io
import matplotlib.pyplot as plt
import cv2
import numpy as np


def getCorner(a):
    """ given list of points gets the coner points

    Arguments:
    a array -- containg arrays with height and width of the point location

    Returns:
        np array  -- [
            ymin, xmin,
            ymax, xmax
        ]
    """
    ymax = a[:, 1].max()
    xmax = a[:, 0].max()
    ymin = a[:, 1].min()
    xmin = a[:, 0].min()

    b = np.array([
        ymin, xmin,
        ymax, xmax
    ])
    return b


def get_location(img_location):
    #### DONT USE ####
    """ given a image with annotaion mask get the locations of those dots 
    
    Arguments:
        img_location {String} -- 
    
    Returns:
        [np array] -- mask
    """
    '''https://stackoverflow.com/questions/49147937/coordinate-location-based-off-pixel-color'''

    mask = io.imread(img_location)
    # COMPUTE MASK current version inacurate 
    return np.nonzero(mask)


def dot_image(img_location, out_path, cordinates):
    """ creates imagees with annotation overlay for inspection 
    
    Arguments:
        img_location {STRING} -- 
        out_path {STRING} -- 
        cordinates {NP ARRAY} -- contanig the points [[x,y]...[xn,yn]]
        
    """''' '''
    img = io.imread(img_location)
    im = np.zeros((img.shape[0], img.shape[1]))
    # print(img)
    for j in cordinates:
        im[j[1]:j[1]+1, j[0]:j[0]+1] = 1

    io.imsave(out_path, im)


def image_spliter(img_path, out_path, step=800):
    """ given a image splits in to spesified steps ex default 800*800 blocks 
    
    Arguments:
        img_path {STRING} -- 
        out_path {STRING} --
    
    Keyword Arguments:
        step {int} -- size of the blocks make sure it fits in the original image (default: {800})
    """
    img = io.imread(img_path)
    # print(os.path.split(img_path))
    for i in range(100, img.shape[0], step):
        for j in range(50, img.shape[1], step):

            if(i+step < img.shape[0] and j+step < img.shape[1]):
                new_img = img[i:i+step, j:j+step]
                io.imsave(out_path+str(i)+"_"+str(j)+"_" +
                          str(os.path.split(img_path)[1]), new_img)


if __name__ == "__main__":
    ims = os.listdir("/media/aich/DATA/canola_flowers/Grow_Pro_Canola_flower/rgb")
    for i in ims:
        print("/media/aich/DATA/canola_flowers/Grow_Pro_Canola_flower/rgb/"+i)
        image_spliter(
            "/media/aich/DATA/canola_flowers/Grow_Pro_Canola_flower/rgb/"+i, "800by800/", step=500)
