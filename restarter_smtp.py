import subprocess
import time
import random
import psutil
import os
import sys
p = psutil.Process(os.getpid())
p.nice(18)



while True:
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    time.sleep(1)
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    time.sleep(1)
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    time.sleep(1)
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    time.sleep(1)
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    time.sleep(1)
    subprocess.run(["python3.10", "./makeScreen2smtpBase.py"]) 
    
    time.sleep(random.randint(1,10))
