#!/usr/bin/env python3

"""
This file is part of the ddcontroller library (https://github.com/ansarid/ddcontroller).
Copyright (C) 2022  Daniyal Ansari

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import math
import time
from ddcontroller import DDRobot

# Create robot object
robot = DDRobot(debug=True)

try:

    # While robot is running
    while robot.running:

        # Set robot's heading to pi/2 with a maximum angular velocity of 1 rad/s
        robot.set_heading(math.pi/2, max_angular_velocity=1)

        # Print the motion of the robot
        print("Target:", robot.target_heading, "Actual:",robot.get_heading())

        # Run loop at 50Hz
        time.sleep(1/50)

except KeyboardInterrupt:
    print('Stopping...')

finally:
    # Clean up.
    robot.stop()
    print('Stopped.')