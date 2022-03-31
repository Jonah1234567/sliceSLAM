import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import numpy as np
from feature_matching.oscillator import oscillate, m_norm_diff
import cv2 as cv
import matplotlib.pyplot as plt

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)

combined_data = pd.read_csv(cfg.get("combined_data_path"))

# combined_data["x_offset"] = ""
# combined_data["y_offset"] = ""
#
# for i in range(len(combined_data) - 1):
#     print(i)
#     image_A = Image.open(combined_data.loc[i, "frame_path"]).convert("L")  # L grayscale
#     image_B = Image.open(combined_data.loc[i + 1, "frame_path"]).convert("L")
#
#     image_A_Data = np.asarray(image_A, dtype="float32")  # maybe do ints instead?
#     image_B_Data = np.asarray(image_B, dtype="float32")
#     x_off, y_off = oscillate(image_A_Data, image_B_Data)
#     combined_data.at[i, "x_offset"] = x_off
#     combined_data.at[i, "y_offset"] = y_off
#
# combined_data.to_csv(cfg.get("combined_data_path"))

img1 = cv.imread('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\data\\output\\images'
                 '\\out0050.png', cv.IMREAD_GRAYSCALE)  # queryImage
img2 = cv.imread('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\data\\output\\images'
                 '\\out0051.png', cv.IMREAD_GRAYSCALE)  # trainImage
# Initiate ORB detector
orb = cv.ORB_create()
# find the key points and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1, des2)
# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)
print(str(matches))
# Draw first 10 matches.
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:100], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3), plt.show()
