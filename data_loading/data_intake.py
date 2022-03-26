import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-f", "--file", help="file to be analyzed", default='C:\\Users\\jonah\\Desktop\\Projects'
                                                                        '\\Programming\\Personal\\sliceSLAM\\data'
                                                                        '\\input\\sample.mp4')
parser.add_argument("-fps", "--fps", help="how many frames to be recorded per second", default='24')

args = parser.parse_args()

frames = str(args.file)
fps = str(args.fps)
output_folder = 'C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\data\\output'
output = os.path.join(output_folder, 'out%04d.png')
print("hi")

for f in os.listdir(output_folder):
    os.remove(os.path.join(output_folder, f))

os.system('ffmpeg -i ' + frames + ' -vf fps=' + fps + ' ' + output)
