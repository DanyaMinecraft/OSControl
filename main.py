import OSControl.OSControl

import os
import time

sleep_time = input("Через сколько уснуть?: ")
time.sleep(float(sleep_time))
os.system("pm-suspend")
