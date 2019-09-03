import matplotlib.pyplot as plt
from skimage import io, color
from skimage.transform import rescale, resize, downscale_local_mean
import os
import skimage.exposure as expo
from PIL import Image
import os
import skimage.io as io


def padding(inpath, outpath, wh):
    """ Adds black padding to get a given set images to a spesified width and height 
        Args:
        inpath (String ): directory containing neded images 
        outpath (String): directory to save modified images 
    """
    for i in os.listdir(inpath):

        img = Image.open(os.path.join(inpath , i), 'r')
        background = Image.new('RGBA', wh, (0, 0, 0, 255))
        offset = (0, 0)
        background.paste(img, offset)
        background.save(os.path.join(outpath , i))


def findMaxWH(inpath):
    """find the max width and height in a given image folder.
    Args:
        inpath (string): directory containing neded images 
    Returns:
        (INT,INT): tuple containgn max  height and width 
    """
    maxW = 1000000000
    maxH = 1000000000
    for i in os.listdir(inpath):
        try:

            img = io.imread(inpath + i)
            maxW = min(maxW, img.shape[0])
            maxH = min(maxH, img.shape[1])

        except:
            pass

    return (maxH, maxW)


def reshape(h, w, in_path, out_path):
    """ given a image reshape it to have the spesified height and witdth. 
    
    Arguments:
        h int -- new heigh in pixels
        w int -- new width in pixels
        in_path string -- path to the folder contaiing origenal images.
        out_path string -- path to  a folder to contain reshaped images.
        
        
    return: None new images are save to the spesified location in out path  
    """

   
    f = os.listdir(in_path)
    for i in f:
        image = io.imread(in_path+i)
        image_resized = resize(image, (h, w),
                               anti_aliasing=True)
        # in case out put images are darker than the original ex in the case of gam reshaping
        image_resized = expo.equalize_adapthist(image_resized)
        io.imsave(os.path.join(out_path,i[:-3]+"PNG"), (image_resized))


def center_crop(in_path, out_path, new_width, new_height):
    """given a new width and a height crop from the center
    
    Arguments:
        in_path string -- path to the folder contaiing origenal images.
        out_path string -- path to  a folder to contain reshaped images.
        new_width Int -- new image width 
        new_height Int -- new image height
    """
    '''
    https://stackoverflow.com/questions/16646183/crop-an-image-in-the-centre-using-pil
    '''
    im = Image.open(in_path)
    width, height = im.size   # Get dimensions

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    im.save(out_path)


if __name__ == "__main__":
    # print(findMaxWH("/media/aich/DATA/wheat_head/800x800/cut/"))
    # padding("/media/aich/DATA/wheat_head/800x800/cut/",
    #         "/media/aich/DATA/wheat_head/800x800/padded/", (3504, 3504))

    center_crop("/media/aich/DATA/wheat_head/800x800/cut/IMG_0402.PNG",
                "/media/aich/DATA/wheat_head/800x800/padded/IMG_0402.PNG", 1600, 2400)
