import time
from mbot_bridge.api import MBot

robot = MBot()

def drive_square():
    for _ in range(4):  # Four sides of a square
        robot.drive(1.0, 0, 0)  # Move forward (vx=1.0), no sideways (vy=0), no rotation (wz=0)
        time.sleep(2)  # Move forward for 2 seconds (adjust this based on your robot's speed)
        robot.drive(0, 0, 1.57)  # Turn 90 degrees (angular velocity wz=1.57 rad/s)
        time.sleep(1)  # Turn for 1 second (adjust as needed for a 90-degree turn)
        
        robot.drive(0, 0, 0)  # Stop before moving to the next side of the square
        time.sleep(0.5)  # Small pause before next move

def drive_square_three_times():
    for _ in range(3):  # Repeat the square driving three times
        drive_square()

# Start the process
drive_square_three_times()

# Stop the robot at the end
robot.stop()