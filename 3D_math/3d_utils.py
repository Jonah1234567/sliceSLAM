import numpy as np
from numpy import array, cross
from numpy.linalg import solve, norm


# variable rename this stuff, your naming scheme is just going to confuse you
def angular_to_threespace_line(x_start, y_start, z_start, theta_rotation, phi_rotation, degrees):
    if degrees:
        theta_rotation, phi_rotation = np.radians(theta_rotation), np.radians(phi_rotation)
    return x_start, y_start, z_start, np.cos(phi_rotation) * np.cos(theta_rotation), np.cos(phi_rotation) * np.cos(
        theta_rotation), np.sin(phi_rotation)


def threespace_to_multipoint_line(x_s, y_s, z_s, x_scale, y_scale, z_scale, length):
    t = length / (x_scale ** 2 + y_scale ** 2 + z_scale ** 2)
    p1 = (x_s, y_s, z_s)
    p2 = (x_s + x_scale * t, y_s + y_scale * t, z_s + z_scale * t)
    return p1, p2


def find_poi(line_A_P1, line_A_P2, line_B_P1, line_B_P2):

    # compute unit vectors of directions of lines A and B
    UA = (line_A_P2 - line_A_P1) / norm(line_A_P2 - line_A_P1)
    UB = (line_B_P2 - line_B_P1) / norm(line_B_P2 - line_B_P1)
    # find unit direction vector for line C, which is perpendicular to lines A and B
    UC = cross(UB, UA);
    UC /= norm(UC)

    # solve the system derived in user2255770's answer from StackExchange: https://math.stackexchange.com/q/1993990
    RHS = line_B_P1 - line_A_P1
    LHS = array([UA, -UB, UC]).T
    print(solve(LHS, RHS))


p1 = np.array([0, 0, 0])
p2 = np.array([10, 10, 10])
p3 = np.array([0, 5, 0])
p4 = np.array([10, 5, 10])
find_poi(p1, p2, p3, p4)
