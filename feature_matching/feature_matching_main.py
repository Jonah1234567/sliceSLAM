import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)

motion_data = pd.read_csv(cfg.get("combined_data_path"))
print(motion_data)

