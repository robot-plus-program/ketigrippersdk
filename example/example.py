#!/usr/bin/env python3

import os, sys
sys.path.append(f"{os.getcwd()}/../include")
from zimmergripper import *

gripper = KetiZimmer(f'{os.getcwd()}/../lib/libzimmergripper.so')
gripper.Connect('192.168.137.254', 502)


