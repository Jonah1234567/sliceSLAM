import numpy as np
from numpy import array, cross
from numpy.linalg import solve, norm


# variable rename this stuff, your naming scheme is just going to confuse you

# clarify what the reference point for the angle with the camera is
def pixel_to_threespace_line(camera_height, camera_width, x_pos, y_pos, z_pos, theta_rot, phi_rot, pixel_x, pixel_y,
                             camera_range_theta, camera_range_phi, degrees=True):
    t_r = pixel_x / camera_width * camera_range_theta + theta_rot
    p_r = pixel_y / camera_height * camera_range_phi + phi_rot
    return angular_to_threespace_line(x_pos, y_pos, z_pos, t_r, p_r, degrees)


def angular_to_threespace_line(x_start, y_start, z_start, theta_rotation, phi_rotation, degrees=True):
    if degrees:
        theta_rotation, phi_rotation = np.radians(theta_rotation), np.radians(phi_rotation)
    normalization = abs(np.cos(phi_rotation) * np.cos(theta_rotation)) + abs(
        np.cos(phi_rotation) * np.cos(theta_rotation)) + abs(np.sin(phi_rotation))

    return x_start, y_start, z_start, np.cos(phi_rotation) * np.cos(theta_rotation) / normalization, np.cos(
        phi_rotation) / normalization * np.cos(
        theta_rotation), np.sin(phi_rotation) / normalization


def threespace_to_multipoint_line(x_s, y_s, z_s, x_scale, y_scale, z_scale, length):
    t = length / (x_scale ** 2 + y_scale ** 2 + z_scale ** 2) ** (1 / 2)
    point1 = (x_s, y_s, z_s)
    point2 = (x_s + x_scale * t, y_s + y_scale * t, z_s + z_scale * t)
    return point1, point2


def multipoint_to_threespace_line(point1, point2):
    x_s, y_s, z_s = point1
    x_scale, y_scale, z_scale = (point2 - point1) / np.sum(np.abs(point2 - point1))

    return x_s, y_s, z_s, x_scale, y_scale, z_scale


def find_distance_and_point(line, point):
    return distance, x_pos, y_pos, z_pos


def find_poi(line_A_P1, line_A_P2, line_B_P1, line_B_P2, length, increment=0.01, threshold=1):
    records = np.zeros((int(length / increment), 4))

    for i in range(len(records)):
        line = multipoint_to_threespace_line(line_A_P1, line_A_P2)
        point = line_B_P1 + (line_B_P2 - line_B_P1) * i / len(records)
        records[i] = find_distance_and_point(line, point)
    return records[np.argmax(records[0])]


p1 = np.array([0, 0, 0])
p2 = np.array([10, 10, 10])
p3 = np.array([0, 5, 0])
p4 = np.array([10, 5, 10])
find_poi(p1, p2, p3, p4, 10)
