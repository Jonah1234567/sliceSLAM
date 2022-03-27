# do image preprocessing here, i.e. crops, transforms, edge detection ...
import numpy as np


def to_grayscale(arr):
    # "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return np.mean(arr, -1)  # average over the last axis (color channels)
    else:
        return arr
