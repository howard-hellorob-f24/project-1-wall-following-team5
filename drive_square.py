import time
from mbot_bridge.api import MBot

robot = MBot()

def drive_square():
    for _ in range(4):  # Four sides of a square
        robot.drive(1.0, 0, 0) #go forward
        time.sleep(0.5)
        robot.drive(0, 0, 1.57)#turn 90 degrees counterclockwise
        time.sleep(1)

    # Stop the robot at the end
    robot.stop()
