import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)

motion_data = pd.read_csv(cfg.get("motion_data_path"))

fps = cfg.get("fps")
frames_per_ms = 1000 / fps

time_counter = 0

combined_data = motion_data
combined_data["frame_path"] = ""
i = 0
for f in os.listdir(cfg.get("output_folder")):
    combined_data.at[i, "frame_path"] = os.path.join(cfg.get("output_folder", f))
    i += 1

combined_data = combined_data.loc[combined_data["frame_path"] != ""]

if len(motion_data) != len(combined_data):
    print("Warning, some data may have been cutout due to mismatched dimensions between frame and motion data")

combined_data.to_csv(cfg.get("combined_data_output_path"))
