# # Sajith Rajapaska
# # last edit : 2019/07/18
# ##################################################################################
# # Step 1. load original images and create the overlay with annotaions
# # Step 2. Split original and overlay images in to x by x slices
# # Step 3. Create annotaion json fils using red dots for the newly split images
# # Step 4. Use the Annotation files to create the Gam images
# # Step 5. Create different veriations of the gam images using reshape
# # End : you should have atleast  4 files ORG: containig split images with no annotaions
# # ANNO: containig json for each image
# # OVL: contaning images with overlay
# # GAM : gam images with the same X BY X size as the org images
# # optional: Gam_8: x/8 by x/8 images , Gam_16 ...
# ###################################################################################

import os
import pandas as pd
import skimage.io as io
from imageSplit import *
from imageReshaping import *
from gen_gam_image import *
from jsonParser import *

base = "/home/sajith/Data/Canola_HR/"
original = "org"
overlay = "Overlay"
data = "Data_FlowerCounts.json"

# # #---------------------------------------------------------------------------------------
# # # get annotations from json
temp = matchDataToImagesSize(
    "/home/sajith/Downloads/floweranno-8f1b1-export (2).json", "/media/aich/DATA/wheat_head/JPEG", "wheat")

save_pickle("wheat_data", temp) # save data
# #---------------------------------------------------------------------------------------
# # #Step 1
new_base = "/media/aich/DATA/wheat_head/800x800/"
if not os.path.exists(new_base):
    os.makedirs(new_base)
    os.makedirs(new_base+"dot")
    os.makedirs(new_base+"cut")
    os.makedirs(new_base+"dot_cut")
    os.makedirs(new_base+"cut_split")
    os.makedirs(new_base+"dot_cut_split")
    os.makedirs(new_base+"anno")
    os.makedirs(new_base+"gam")
    os.makedirs(new_base+"gam_8")

