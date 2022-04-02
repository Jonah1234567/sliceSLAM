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


def pixel_to_multipoint_line(camera_height, camera_width, camera_range_theta, camera_range_phi, x_pos, y_pos, z_pos,
                             theta_rot, phi_rot, pixel_x, pixel_y, degrees=True, length=10):
    temp = pixel_to_threespace_line(camera_height, camera_width, x_pos, y_pos, z_pos, theta_rot, phi_rot, pixel_x,
                                    pixel_y, camera_range_theta, camera_range_phi, degrees)
    return threespace_to_multipoint_line(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], length)


def angular_to_threespace_line(x_start, y_start, z_start, theta_rotation, phi_rotation, degrees=True):
    if degrees:
        theta_rotation, phi_rotation = np.radians(theta_rotation), np.radians(phi_rotation)
    normalization = abs(np.cos(phi_rotation) * np.cos(theta_rotation)) + abs(
        np.cos(phi_rotation) * np.cos(theta_rotation)) + abs(np.sin(phi_rotation))
    x_scale = np.cos(phi_rotation) * np.cos(theta_rotation) / normalization
    y_scale = np.cos(phi_rotation) * np.sin(theta_rotation) / normalization
    z_scale = np.sin(phi_rotation) / normalization
    return x_start, y_start, z_start, x_scale, y_scale, z_scale


def threespace_to_multipoint_line(x_s, y_s, z_s, x_scale, y_scale, z_scale, length):
    t = length / (x_scale ** 2 + y_scale ** 2 + z_scale ** 2) ** (1 / 2)
    point1 = (x_s, y_s, z_s)
    point2 = (x_s + x_scale * t, y_s + y_scale * t, z_s + z_scale * t)
    return point1, point2


def multipoint_to_threespace_line(point1, point2):
    x_s, y_s, z_s = point1
    x_scale, y_scale, z_scale = (point2 - point1) / np.sum(np.abs(point2 - point1))

    return x_s, y_s, z_s, x_scale, y_scale, z_scale


def multi_dimension_pythagorean(arr):
    return np.power(np.sum(np.power(arr, 2)), 1/2)


def normalize(arr):
    return arr/multi_dimension_pythagorean(arr)


def find_distance_and_point(A, B, C):
    # copied from stack
    # https://stackoverflow.com/questions/56463412/distance-from-a-point-to-a-line-segment-in-3d-python
    distance = multi_dimension_pythagorean(np.cross(A-B, C-B)) / multi_dimension_pythagorean(C-B)

    tangent = normalize(np.cross(np.cross(A-B, C-B), C-B))
    point = A + tangent/2*distance
    print(point)
    return distance, point


def find_poi(line_A_P1, line_A_P2, line_B_P1, line_B_P2, length, step_size=0.01, threshold=1):
    line_A_P1, line_A_P2, line_B_P1, line_B_P2 = np.array(line_A_P1), np.array(line_A_P2), np.array(
        line_B_P1), np.array(line_B_P2)
    records = np.zeros((int(length / step_size)))
    points_records = np.zeros((int(length / step_size), 3))

    for i in range(len(records)):
        point = line_B_P1 + (line_B_P2 - line_B_P1) * i / len(records)

        dist, mid_point = find_distance_and_point(point, line_A_P1, line_A_P2)

        if abs(dist) <= 0.001:
            return 0, mid_point

        records[i] = dist
        points_records[i] = mid_point
    print(points_records)
    return records[np.argmin(records)], points_records[np.argmin(records)]


def find_intersection(camera, start_pos1, start_pos2, pixel_loc1, pixel_loc2, degrees=True, length=10, step_size=0.01,
                      threshold=1):
    p1, p2 = pixel_to_multipoint_line(camera[0], camera[1], camera[2], camera[3], start_pos1[0], start_pos1[1],
                                      start_pos1[2], start_pos1[3], start_pos1[4], pixel_loc1[0], pixel_loc1[1],
                                      degrees, length)
    p3, p4 = pixel_to_multipoint_line(camera[0], camera[1], camera[2], camera[3], start_pos2[0], start_pos2[1],
                                      start_pos2[2], start_pos2[3], start_pos2[4], pixel_loc2[0], pixel_loc2[1],
                                      degrees, length)
    return find_poi(p1, p2, p3, p4, length, step_size, threshold)


cam = np.array((1080, 1920, 70, 45))
sp_1 = np.array((0, 0, 0, 0, 0))
pl1 = np.array((0, 0))
sp_2 = np.array((1, 1, 0, 0, 0))
pl2 = np.array((500, 0))
print(find_intersection(cam, sp_1, sp_2, pl1, pl2))
