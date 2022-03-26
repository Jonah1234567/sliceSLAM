import os
import yaml
from yaml.loader import SafeLoader

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    data = yaml.load(f, Loader=SafeLoader)

frames = data.get("video_path")
fps = str(data.get("fps"))
output_folder = data.get("output_folder")
output = os.path.join(output_folder, data.get("frame_name"))

for f in os.listdir(output_folder):
    os.remove(os.path.join(output_folder, f))

os.system('ffmpeg -i ' + frames + ' -vf fps=' + fps + ' ' + output)
os.system(data.get("merge"))
