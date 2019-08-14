import time
import sys

dep_path = 'E:\\github\\ragan-git\\touchdesigner\\_workshops\\_summit-2019\\touchdesigner-summit-2019-external-python\\workshop\\dep\\python'
divider = '- ' * 10

for each in sys.path:
    print(each)

print(divider)

if dep_path not in sys.path:
    sys.path.append(dep_path)

for each in sys.path:
    print(each)

time.sleep(120)