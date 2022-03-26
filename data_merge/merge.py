import numpy as np
import os
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg= yaml.load(f, Loader=SafeLoader)

motion_data = np.genfromtxt(cfg.get("motion_data_path"), dtype=None, delimiter=',', skip_header=1)

fps = cfg.get("fps")
frames_per_ms = 1000/fps

time_counter = 0
for f in os.listdir(cfg.get("output_folder")):
    

