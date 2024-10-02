import time
from mbot_bridge.api import MBot

robot = MBot()

# Constants for speed and timing
VELOCITY_X = 0.4  # Forward velocity (in inches per second)
TURN_SPEED = 1.57  # Angular velocity (rad/s) for 90-degree turns
SIDE_LENGTH = 2.0  # Length of one side of the square in inches 
DRIVE_TIME = SIDE_LENGTH / VELOCITY_X  # Time to drive one side of the square based on speed and distance

# Adjust the TURN_TIME for sharper turns
TURN_TIME = 1.2   # Increased time to turn 90 degrees, fine-tune this as needed
REPEAT_SQUARE = 3  # Number of times to repeat the square

def drive_square():
    for _ in range(4):  # Four sides of the square
        # Move forward
        robot.drive(VELOCITY_X, 0, 0)  # Move forward
        time.sleep(DRIVE_TIME)  # Drive for the calculated time to cover one side
        robot.drive(0, 0, TURN_SPEED)  # Turn 90 degrees counterclockwise
        time.sleep(TURN_TIME)  # Time to turn 90 degrees (adjusted)
        
        # Stop the robot briefly before moving to the next side
        robot.drive(0, 0, 0)  # Stop the robot
        time.sleep(0.2)  # Small pause to ensure smoother transitions

def drive_square_three_times():
    for _ in range(REPEAT_SQUARE):  # Repeat the square-driving pattern 3 times
        drive_square()

# Use try-except to handle Ctrl + C
try:
    # Start the process
    drive_square_three_times()
except KeyboardInterrupt:
    print("\nProcess interrupted. Stopping the robot.")
    robot.stop()  # Ensure the robot stops if the program is interrupted
finally:
    robot.stop()  # Ensure the robot is always stopped, even if there's an error
