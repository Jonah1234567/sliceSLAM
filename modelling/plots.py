import pandas as pd
import os
import yaml
from yaml.loader import SafeLoader
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Open the file and load the file
with open('C:\\Users\\jonah\\Desktop\\Projects\\Programming\\Personal\\sliceSLAM\\config.YAML') as f:
    cfg = yaml.load(f, Loader=SafeLoader)
combined_data = pd.read_csv(cfg.get("combined_data_path"))


def get_drone_data():
    drone_points_x = np.zeros((len(combined_data)))
    drone_points_y = np.zeros((len(combined_data)))
    drone_points_z = np.zeros((len(combined_data)))
    for i in range(len(combined_data)):
        drone_points_x[i] = np.array((combined_data.loc[i, "X_Pos"]))
        drone_points_y[i] = combined_data.loc[i, "Y_Pos"]
        drone_points_z[i] = combined_data.loc[i, "Z_Pos"]
    return drone_points_x, drone_points_y, drone_points_z


def plot(line, scatter, x, y, z, x2=np.array(0), y2=np.array(0), z2=np.array(0), drone_path=False):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    if scatter:
        ax.scatter3D(x, y, z, cmap='Greens')
        if drone_path:
            ax.scatter3D(x2, y2, z2, cmap='Blue')
        plt.show()

    if line:
        ax.plot3D(x, y, z, 'gray')
        if drone_path:
            ax.plot3D(x2, y2, z2, 'blue')
        plt.show()


def plot_drone(line=False, scatter=True):
    x, y, z = get_drone_data()
    plot(line, scatter, x, y, z)


def environment_plotter(drone_path=True, scatter=True, line=False):
    env_data = np.genfromtxt(cfg.get("environment_data"), delimiter=',')
    x, y, z = env_data[:, 0], env_data[:, 1], env_data[:, 2]

    if drone_path:
        dx, dy, dz = get_drone_data()
        plot(line, scatter, x, y, z, dx, dy, dz, drone_path)
    else:
        plot(line, scatter, x, y, z)


