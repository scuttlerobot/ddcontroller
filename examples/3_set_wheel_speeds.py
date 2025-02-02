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

import time
import numpy as np
from ddcontroller.wheels import Wheel

# Create right wheel object
wheel = Wheel(motor_pins=(11, 12),
              pwm_frequency=220,
              i2c_bus=1,
              encoder_address=0x40,
              wheel_radius=0.04165,
              motor_pulley_teeth=15,
              wheel_pulley_teeth=30,
              )

try:

    # Create infinite loop
    while True:

        # Update wheel measurements
        wheel.update()

        # Print current wheel angular velocity
        print('{}'.format(wheel.get_angular_velocity()))

        # Set wheel angular velocity to 2*pi
        wheel.set_angular_velocity(2*np.pi)

        # Run loop at 50Hz
        time.sleep(1/50)

except KeyboardInterrupt:

    print('Stopping...')

finally:
    # Clean up.
    wheel.stop()
    print('Stopped.')