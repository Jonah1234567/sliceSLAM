import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import numpy as np

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)

combined_data = pd.read_csv(cfg.get("combined_data_path"))

#for i in range(len(combined_data) - 1):

for i in range(50,51):
    image_A = Image.open(combined_data.loc[i, "frame_path"]).convert("L")  # L grayscale
    image_B = Image.open(combined_data.loc[i + 1, "frame_path"]).convert("L")

    image_A_Data = np.asarray(image_A, dtype="float32") # maybe do ints instead?
    image_B_Data = np.asarray(image_B, dtype="float32")
    print(np.shape(image_A_Data))
    diff = image_A_Data - image_B_Data  # elementwise for np array
    m_norm = sum(sum(abs(diff)))  # Manhattan norm



