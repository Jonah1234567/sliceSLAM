import numpy as np
# move the second image not the first image

def oscillator(im1, im2):
    min_diff = 9999999999
    best_x, best_y = 0, 0
    for x in range(-50, 51, 10): # this is pure jank
        for y in range(-50, 51, 10):
            temp_diff = m_norm_diff()
            if temp_diff<min_diff:
                min_diff = temp_diff
                best_x, best_y = x, y
    return best_x, best_y


def m_norm_diff(im1, im2): #manhattan normalization
    if np.shape(im1) != np.shape(im2):
        print("Warning submitted images do not match, fix this")
        return 9999999999
    norm_factor = len(im1)*len(im1[0])
    diff = im1 -im2 # elementwise for np array
    return sum(sum(abs(diff)))/norm_factor