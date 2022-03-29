import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import numpy as np
from feature_matching.oscillator import oscillate, m_norm_diff

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)

combined_data = pd.read_csv(cfg.get("combined_data_path"))


combined_data["x_offset"] = ""
combined_data["y_offset"] = ""


for i in range(len(combined_data) - 1):
    print(i)
    image_A = Image.open(combined_data.loc[i, "frame_path"]).convert("L")  # L grayscale
    image_B = Image.open(combined_data.loc[i + 1, "frame_path"]).convert("L")

    image_A_Data = np.asarray(image_A, dtype="float32")  # maybe do ints instead?
    image_B_Data = np.asarray(image_B, dtype="float32")
    x_off, y_off = oscillate(image_A_Data, image_B_Data)
    combined_data.at[i, "x_offset"] = x_off
    combined_data.at[i, "y_offset"] = y_off

combined_data.to_csv(cfg.get("combined_data_path"))
