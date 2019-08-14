import time
import sys

divider = '- ' * 10

for each in sys.path:
    print(each)

print(divider)

for each in range(10):
    print(each)

time.sleep(120)