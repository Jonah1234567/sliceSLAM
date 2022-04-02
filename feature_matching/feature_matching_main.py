import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import numpy as np
from feature_matching.oscillator import oscillate, m_norm_diff
from spacial_math.math_utils import find_intersection
from modelling.plots import plot_drone, environment_plotter
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


camera = 720, 1280, 72, 40.5
good_points = np.zeros((1, 3))
np.savetxt(cfg.get("environment_data"), good_points, delimiter=",")

for i in range(len(combined_data) - 1):
    print("frame ", i)
    img1 = cv.imread(combined_data.loc[i, "frame_path"], cv.IMREAD_GRAYSCALE)  # queryImage
    img2 = cv.imread(combined_data.loc[i + 1, "frame_path"], cv.IMREAD_GRAYSCALE)  # trainImage
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
    good_points_1 = np.zeros((1, 3))
    for match in matches:

        p1 = kp1[match.queryIdx].pt
        p2 = kp2[match.trainIdx].pt
        point1 = int(round(p1[0])), int(round(p1[1]))
        point2 = int(round(p2[0])), int(round(p2[1]))  # unnecessary?

        sp1 = combined_data.loc[i, "X_Pos"], combined_data.loc[i, "Y_Pos"], combined_data.loc[i, "Z_Pos"], \
              combined_data.loc[i, "Theta_Rot"], combined_data.loc[i, "Phi_Rot"]
        sp2 = combined_data.loc[i + 1, "X_Pos"], combined_data.loc[i + 1, "Y_Pos"], combined_data.loc[i + 1, "Z_Pos"], \
              combined_data.loc[i + 1, "Theta_Rot"], combined_data.loc[i + 1, "Phi_Rot"]
        dist, data = find_intersection(camera, sp1, sp2, point1, point2)
        arr = np.zeros((1, 3))
        arr[0:3] = data[0], data[1], data[2]
        good_points_1 = np.append(good_points_1, arr, axis=0)
    good_points = np.append(good_points, good_points_1, axis=0)
np.savetxt(cfg.get("environment_data"), good_points, delimiter=",")

plot_drone(False, True)
environment_plotter(False, True, True)

