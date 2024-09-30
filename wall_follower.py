import time
import numpy as np
from mbot_bridge.api import MBot

def find_min_dist(ranges, thetas):
    """Finds the length and angle of the minimum ray in the scan."""
    min_dist, min_angle = float('inf'), None
    min_index = np.argmin(ranges)
    min_dist = ranges[min_index] 
    min_angle = thetas[min_index]
    return min_dist, min_angle

def cross_product(min_angle):
    v_to_wall = np.array([np.cos(min_angle), np.sin(min_angle), 0])
    v_up = np.array([0, 0, 1])
    v_forward = np.cross(v_to_wall, v_up)
    return v_forward

# Initialize the robot
robot = MBot()

# Parameters
setpoint = 0.5  # Desired distance from the wall in meters
kp = 1.0        # Proportional gain for wall-following control
min_safe_dist = 0.3  # Minimum safe distance to avoid hitting the wall
max_safe_dist = 0.7  # Maximum safe distance to prevent moving too far from the wall

try:
    while True:
        # Read the latest lidar scan
        ranges, thetas = robot.read_lidar()

        # Find the minimum distance and the corresponding angle
        min_dist, min_angle = find_min_dist(ranges, thetas)

        if min_dist is None or min_dist == float('inf'):
            # No valid distances, skip this iteration
            continue

        # Ensure that the robot doesn't react to obstacles that are too far
        if min_dist < min_safe_dist:
            # If the robot is too close to the wall, stop or reverse
            print("Too close to the wall, adjusting...")
            robot.drive(0, 0)  # Stop to avoid collision
            time.sleep(0.5)
            continue
        elif min_dist > max_safe_dist:
            # If the robot is too far from the wall, turn toward it more aggressively
            angular_velocity = kp * (setpoint - min_dist)
            forward_velocity = 0.15  # Slow forward speed
        else:
            # Normal wall-following behavior
            error = setpoint - min_dist
            angular_velocity = kp * error
            forward_velocity = 0.2  # Normal forward speed

        # Move the robot: pass both the forward velocity and angular velocity
        robot.drive(forward_velocity, angular_velocity)

        # Optionally, print out debug info
        print(f"Min Distance: {min_dist:.2f} m, Angle: {min_angle:.2f} rad, Angular Velocity: {angular_velocity:.2f}")

        # Sleep for a bit before reading a new scan
        time.sleep(0.1)

except KeyboardInterrupt:
    # Stop the robot when the user interrupts the program
    robot.stop()
    
