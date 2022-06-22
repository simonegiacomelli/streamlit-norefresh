from pathlib import Path

print(__file__)
import os
from glob import glob

# result = [y for x in os.walk('.') for y in glob(os.path.join(x[0], '*.*'))]
os.system('mount')
# for r in result:
#     print(r)

hn = Path('/etc/hostname').read_text()
print('hostname', hn)
import time

counter = 0
while True:
    counter += 1
    print(counter)
    time.sleep(5)
