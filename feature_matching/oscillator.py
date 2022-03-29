import numpy as np
from numba import jit, cuda


# move the second image not the first image

@jit(forceobj=True, target_backend='CUDA')
def oscillate(im1, im2):
    min_diff = 9999999999
    best_x, best_y = 0, 0
    for x in range(-50, 51, 10):  # this is pure jank, don't do grid search in the feature, or at least at first
        for y in range(-50, 51, 10):

            im_xi, im_xf, im_yi, im_yf = 0, 0, 0, 0  # better way to orient the different images?
            if x > 0:
                im_xi, im_xf = x, 0
            elif x < 0:
                im_xi, im_xf = 0, x

            if y > 0:
                im_yi, im_yf = y, 0
            elif y < 0:
                im_yi, im_yf = 0, y

            im1_x, im1_y = np.shape(im1)
            im2_x, im2_y = np.shape(im2)

            temp_diff = m_norm_diff(im1[0 + im_xi:im1_x + im_xf, 0 + im_yi:im1_y + im_yf],
                                    im2[0 - im_xf:im2_x - im_xi, 0 - im_yf:im2_y - im_yi])  # have fun
            # understanding this later

            if temp_diff < min_diff:
                min_diff = temp_diff
                best_x, best_y = x, y

    for x in range(best_x - 5, best_x + 6, 1):  # double-check the 6
        for y in range(best_y - 5, best_y + 6, 1):  # double-check the 6

            im_xi, im_xf, im_yi, im_yf = 0, 0, 0, 0  # better way to orient the different images?
            if x > 0:
                im_xi, im_xf = x, 0
            elif x < 0:
                im_xi, im_xf = 0, x

            if y > 0:
                im_yi, im_yf = y, 0
            elif y < 0:
                im_yi, im_yf = 0, y

            im1_x, im1_y = np.shape(im1)
            im2_x, im2_y = np.shape(im2)

            temp_diff = m_norm_diff(im1[0 + im_xi:im1_x + im_xf, 0 + im_yi:im1_y + im_yf],
                                    im2[0 - im_xf:im2_x - im_xi, 0 - im_yf:im2_y - im_yi])  # have fun
            # understanding this later

            if temp_diff < min_diff:
                min_diff = temp_diff
                best_x, best_y = x, y

    return best_x, best_y


def m_norm_diff(im1, im2):  # manhattan normalization
    if np.shape(im1) != np.shape(im2):
        print("Warning submitted images do not match, fix this")
        return 9999999999
    norm_factor = len(im1) * len(im1[0])
    diff = im1 - im2  # elementwise for np array
    return sum(sum(abs(diff))) / norm_factor
