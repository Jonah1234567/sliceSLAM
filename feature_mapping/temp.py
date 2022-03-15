import numpy as np


def calculate_pixel_location_3d(camera1, camera2, pixel1, pixel2, im_length, im_width, im_theta, im_phi):
    x2, y2, z2, theta2, phi2 = camera2
    pixel1_x, pixel1_y = pixel1
    pixel2_x, pixel2_y = pixel2


def create_3d_line(camera, pixel, im_length, im_width, im_theta, im_phi):
    line_x, line_y, line_z, camera_theta, camera_phi = camera
    pixel_x, pixel_y = pixel
    # theta slope corresponds to the x and y plane
    # phi slope corresponds to the x and z plane
    line_theta_slope = np.tan(np.radians(camera_theta + pixel_x/im_length*im_theta))
    line_phi_slope = np.tan(np.radians(camera_phi + pixel_y/im_width*im_phi))
    return line_x, line_y, line_z, line_theta_slope, line_phi_slope


def intersection_point(line1, line2, threshold):
    line_x1, line_y1, line_z1, line_theta_slope1, line_phi_slope1 = line1
    line_x2, line_y2, line_z2, line_theta_slope2, line_phi_slope2 = line2

    continue_condition, i = True, 0

    while continue_condition:
        point_1 = line_x1 +
        i += 1
    # not doing exact intersection point because odds are the lines will not perfectly intersect







