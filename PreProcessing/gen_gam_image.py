'''
python adaptation of https://github.com/littleaich/heatmap-regulation/blob/master/codes/worldexpo/gen_gam_image.m
'''
import numpy as np
import scipy.stats as st
import math


def array_comp(condition_array, ori, replace):
    """ 
    given a condiational array returns a array containing values according to the condition 
    
    Arguments:
        condition_array bool array ex tmp < dhsize
        ori {[type]} -- original arrray contaning the values 
        replace {[type]} -- item to be replaced with 
    
    Returns:
        np array containg items that stasfies the condition. 
    """'''

    '''
    invert_condition_array = np.invert(condition_array)
    ori = ori * invert_condition_array
    condition_array = condition_array * replace
    ori = ori + condition_array
    return ori


def matlab_style_gauss2D(shape=(3, 3), sigma=0.5):
    """taken from https://stackoverflow.com/questions/17190649/how-to-obtain-a-gaussian-filter-in-python 
	python implimentation of  fspecial('gaussian',[shape],[sigma]) 

    
    Keyword Arguments:
        shape {tuple} -- [description] (default: {(3, 3)})
        sigma {float} -- [description] (default: {0.5})
    
    Returns:
        np array --  returns a rotationally symmetric Gaussian lowpass filter of size hsize with standard 
        deviation sigma. 
    """

    m, n = [(ss - 1.) / 2. for ss in shape]
    y, x = np.ogrid[-m:m + 1, -n:n + 1]
    h = np.exp(-(x * x + y * y) / (2. * sigma * sigma))
    h[h < np.finfo(h.dtype).eps * h.max()] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


def gen_gam_image(num_rows, num_cols, center_set, hsize_gauss):
    """Given a height and a width, point locations and the shape of a gaussian returns array containig  
    the GAM 
    Arguments:
        num_rows int -- height of the image
        num_cols int -- width of the image
        center_set [(int,int)] -- list of tuples containing the point locations
        hsize_gauss int -- size of the Gausing filter 
    
    Returns:
        np array - contanig the GAM
    """"""

    """

    if(hsize_gauss % 2) == 0:
        hsize_gauss = hsize_gauss + 1

    sigma = hsize_gauss / (1.96 * 1.5)
    h_gauss = matlab_style_gauss2D((hsize_gauss, hsize_gauss), sigma)
    h_gauss = h_gauss / h_gauss.max()
    # center_set = (N,2) center matrix (c_center, r_center)
    im = np.zeros((num_rows, num_cols))

    if not(center_set.size == 0):
        dhsize = (hsize_gauss - 1) / 2

        # border adjustment
        tmp = center_set[:, 0]
        tmp = array_comp(tmp < dhsize + 1, tmp, dhsize + 1)
        tmp = array_comp(tmp > num_cols - dhsize, tmp, num_cols - dhsize)
        center_set[:, 0] = tmp
        tmp = center_set[:, 1]
        tmp = array_comp(tmp < dhsize + 1, tmp, dhsize + 1)
        tmp = array_comp(tmp > num_rows - dhsize, tmp, num_rows - dhsize)
        center_set[:, 1] = tmp
    

        for i in range(0, center_set.shape[0]):
            cmin = int((center_set[i, 0] - dhsize))
            rmin = int((center_set[i, 1] - dhsize)) - 1
            cmax = int((center_set[i, 0] + dhsize))
            rmax = int((center_set[i, 1] + dhsize))
            if((cmax + 1) - cmin > (rmax - rmin)):
                rmin = rmin + 1
            elif((cmax + 1) - cmin < (rmax - rmin)):
                cmax = cmax + 1
            try:
                im[rmin:(rmax), cmin:cmax + 1] = (im[rmin:(rmax), cmin:cmax + 1] +
                                              h_gauss)
            except: # in some cases cmax or rmax goes outof bounds. quick hack to fix that situation
                pass

        # clip joint activations in between objects
    im = array_comp(im > 1, im, 1)
    # im = bsxfun(@rdivide, im, max(im(:))) % noramlize GAM
    im = im / im.max()
   

    return im


if __name__ == '__main__':

   pass 

