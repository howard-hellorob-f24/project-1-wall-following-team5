import time
from mbot_bridge.api import MBot

robot = MBot()

# Constants
VELOCITY_X = 0.5  # Slower forward velocity (in inches per second)
TURN_SPEED = 0.3  # Slower angular velocity (adjust based on desired turning speed)
DRIVE_TIME = 4.0  # Time to drive 8 inches (adjust based on speed, increased due to slower velocity)
TURN_TIME = 1.5   # Adjusted time to turn 90 degrees (slower turn)
REPEAT_SQUARE = 3  # Number of times to repeat the square

def drive_square():
    for _ in range(4):  # Four sides of a square
        # Move forward
        robot.drive(VELOCITY_X, 0, 0)  # Move forward (vx=VELOCITY_X), no sideways (vy=0), no rotation (wz=0)
        time.sleep(DRIVE_TIME)  # Drive for the time to cover 8 inches
        robot.drive(0, 0, TURN_SPEED)  # Turn 90 degrees with slower speed
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
