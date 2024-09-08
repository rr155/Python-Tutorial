#while loop - good for infinite number of loop. Or repeat for unknown number of times 
"""number = 1 
while number <200:
    # print(number)
    number = number*2
"""

import os 
import subprocess
import time 

while True:
    print("Welcome to monitoring services")
    time.sleep(2)
    cmd = 'tasklist /fi "imagename eq {}"'.format("taskmgr.exe")
    print(cmd)
    output = subprocess.check_output(cmd).decode()
    print(output)
    if 'INFO: No tasks are running' in output:
        print("task was killed please look")
        break # breaks the loop , even infinite one. Can be used with loops only 
    
