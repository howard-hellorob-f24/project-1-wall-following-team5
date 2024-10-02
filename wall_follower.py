from cmath import *
import time
import numpy as np
from mbot_bridge.api import MBot


def find_min_dist(ranges, thetas):
    """Finds the length and angle of the minimum ray in the scan.

    Make sure you ignore any rays with length 0! Those are invalid.

    Args:
        ranges (list): The length of each ray in the Lidar scan.
        thetas (list): The angle of each ray in the Lidar scan.

        

        "Notes"
        - Assuming information will be in this type of format
        ranges = [1.5, 0.0, 2.3, 1.2, 0.0, 3.4]
        thetas = [0, 15, 30, 45, 60, 75]
        -thus each range has a corresponding angle at x index in thetas

    Returns:
        tuple: The length and angle of the shortest ray in the Lidar scan.
    """

    index = 0
    shortest = ranges[0]
    for i in ranges:
        if i < shortest and i != 0:
            shortest = i
            index = ranges.index(i)

    min_dist, min_angle = shortest, thetas[index]

    # TODO: Find the length and angle of the shortest distance in the ray.

    return min_dist, min_angle


def cross_product(v1, v2):
    """Compute the Cross Product between two vectors.

    Args:
        v1 (list): First vector of length 3.
        v2 (list): Second vector of length 3.

        Cross Product Formula:
        cx = aybz-azby
        cy = azbx-axbz
        cz = axby-aybx

    Returns:
        list: The result of the cross product operation.
    """
    cx = v1[1] * v2[2] - v1[2] * v2[1]
    cy = v1[2] * v2[0] - v1[0] * v2[2]
    cz = v1[0] * v2[1] - v1[1] * v2[0]
    res = [cx, cy, cz]
    # TODO: Compute the cross product.
    return res


robot = MBot()
setpoint = 1  # TODO: Pick your setpoint.
# TODO: Declare any other variables you might need here.

try:
    while True:
        # Read the latest lidar scan.
        ranges, thetas = robot.read_lidar()

        # TODO: (P1.2) Write code to follow the nearest wall here.
        # Hint: You should use the functions cross_product and find_min_dist.
        #Find the min distance and angle
        min_dist, min_angle = find_min_dist(ranges, thetas)

        #Cross Product
        v_wall = [1*cos(min_angle), 1*sin(min_angle), 0] #x, y, z, this is the vector the robot will be driving to the wall
        up_vector = [0, 0, 1]
        cross = cross_product(v_wall, up_vector) #forward velocity vector

        #Correction Vector
        if cross[0] < setpoint:
            correction_vector = [setpoint, 0, 0]

        #final control command
        final_v = [cross[0] + correction_vector[0], cross[1] + correction_vector[1], cross[2] + correction_vector[2]]
        robot.drive(final_v[0], final_v[1], final_v[2])
        # Optionally, sleep for a bit before reading a new scan.
        time.sleep(0.1)
except:
    # Catch any exception, including the user quitting, and stop the robot.
    robot.stop()
