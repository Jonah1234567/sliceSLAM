import PIL
import numpy as np
from matplotlib import pyplot as plt


def difference_mapper(im_path1, im_path2):
    # accepts two image paths and loads the images through the pillow library
    # images are converted into numpy arrays and the absolute difference in their
    # pixel values are found and those differences are inserted as new pixel
    # values
    im1 = PIL.Image.open(im_path1)
    im_arr1 = np.array(im1)

    im2 = PIL.Image.open(im_path2)
    im_arr2 = np.array(im2)

    # error catch for not matching dimensions
    if np.shape(im_arr1) == np.shape(im_arr2):
        result = np.abs(im_arr1 - im_arr2)
        return result

    else:
        print("dimensions do not match, error")
        return -999


def image_values(im_path1):
    im1 = PIL.Image.open(im_path1)
    im_arr1 = np.array(im1)
    return im_arr1


def single_channel_difference_mapper(im_path1, im_path2):
    # accepts two image paths and loads the images through the pillow library
    # images are converted into numpy arrays and the absolute difference in their
    # pixel values are found and those differences are inserted as new pixel
    # values
    im1 = PIL.Image.open(im_path1).convert('L')
    im_arr1 = np.array(im1)

    im2 = PIL.Image.open(im_path2).convert('L')
    im_arr2 = np.array(im2)

    # error catch for not matching dimensions
    if np.shape(im_arr1) == np.shape(im_arr2):
        result = np.abs(im_arr1 - im_arr2)
        return result

    else:
        print("dimensions do not match, error")
        return -999


def mean_difference_value(difference_map):
    return np.mean(difference_map)


def mean_log_difference_value(difference_map):
    return np.mean(np.log10(difference_map))


def mean_squared_difference_value(difference_map):
    return np.mean(difference_map ** 2)


def display_difference_map(difference_map):
    plt.imshow(difference_map, interpolation='nearest')
    plt.show()


def histogram_difference_map(difference_map):
    plt.hist(difference_map)
    plt.show()


d_map = single_channel_difference_mapper("C:\\Users\\jonah\\PycharmProjects\\sliceSLAM\\Sample Drone "
                                         "Video\\thumb0002.jpg",
                                         "C:\\Users\\jonah\\PycharmProjects\\sliceSLAM\\Sample Drone "
                                         "Video\\thumb0003.jpg")


print(mean_difference_value(d_map))
print(np.shape(d_map), np.max(d_map), np.min(d_map))
