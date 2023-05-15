import time
import sys


for i in reversed(range(11)):
    time.sleep(1)
    sys.stdout.write(f'\r {i}')
