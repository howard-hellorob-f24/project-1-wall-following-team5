import time
import numpy as np
from mbot_bridge.api import MBot

def find_min_dist(ranges, thetas):
    """Finds the length and angle of the minimum ray in the scan."""
    min_dist, min_angle = float('inf'), None
    for i, dist in enumerate(ranges):
        if dist > 0:  # Ignore invalid ranges (e.g., zero or negative)
            if dist < min_dist:
                min_dist = dist
                min_angle = thetas[i]
    return min_dist, min_angle

def cross_product(v1, v2):
    """Compute the Cross Product between two vectors (unused in this task)."""
    res = np.zeros(3)
    res[0] = v1[1] * v2[2] - v1[2] * v2[1]
    res[1] = v1[2] * v2[0] - v1[0] * v2[2]
    res[2] = v1[0] * v2[1] - v1[1] * v2[0]
    return res

# Initialize the robot
robot = MBot()

# Parameters
setpoint = 0.5  # Desired distance from the wall in meters
kp = 0.5        # Proportional gain for wall-following control

try:
    while True:
        # Read the latest lidar scan
        ranges, thetas = robot.read_lidar()

        # Find the minimum distance and the corresponding angle
        min_dist, min_angle = find_min_dist(ranges, thetas)
        
        if min_dist is None or min_dist == float('inf'):
            # No valid distances, skip this iteration
            continue
        
        # Compute the error (how far the robot is from the desired setpoint)
        error = setpoint - min_dist

        # Proportional control: adjust turning rate based on the error
        angular_velocity = kp * error
        
        # Move the robot: turn towards/away from the wall based on angular velocity
        forward_velocity = 0.2  # Move forward at a constant speed
        robot.drive(forward_velocity, angular_velocity)

        # Optionally, print out debug info
        print(f"Min Distance: {min_dist:.2f} m, Angle: {min_angle:.2f} rad, Error: {error:.2f}, Angular Velocity: {angular_velocity:.2f}")
        
        # Sleep for a bit before reading a new scan
        time.sleep(0.1)

except KeyboardInterrupt:
    # Stop the robot when the user interrupts the program
    robot.stop()
