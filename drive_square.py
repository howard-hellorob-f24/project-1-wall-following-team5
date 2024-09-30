import time
from mbot_bridge.api import MBot

robot = MBot()

# Constants
VELOCITY_X = 1.0  # Forward velocity in inches per second (adjust based on actual speed)
TURN_SPEED = 0.5  # Angular velocity (adjust based on how fast the robot turns)
DRIVE_TIME = 2.0  # Time to drive 8 inches (adjust based on speed)
TURN_TIME = 1.0   # Time to turn 90 degrees (adjust based on turning speed)
REPEAT_SQUARE = 3  # Number of times to repeat the square

def drive_square():
    for _ in range(4):  # Four sides of a square
        # Move forward
        robot.drive(VELOCITY_X, 0, 0)  # Move forward (vx=VELOCITY_X), no sideways (vy=0), no rotation (wz=0)
        time.sleep(DRIVE_TIME)  # Drive for the time to cover 8 inches
        robot.drive(0, 0, TURN_SPEED)  # Turn 90 degrees
        time.sleep(TURN_TIME)  # Time to turn 90 degrees
        
        # Stop the robot briefly before the next side
        robot.drive(0, 0, 0)  # Stop
        time.sleep(0.5)  # Small pause

def drive_square_three_times():
    for _ in range(REPEAT_SQUARE):  # Repeat the square 3 times
        drive_square()

# Start the process
drive_square_three_times()

# Stop the robot at the end
robot.stop()
