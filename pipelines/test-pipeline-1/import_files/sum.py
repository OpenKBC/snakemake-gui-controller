from sys import argv
import time

count_start = 0
with open(argv[1], "r") as f:
    for line in f.readlines():
        count_start+=int(line)

time.sleep(3)

with open(argv[2], "w") as rw:
    rw.write(str(count_start))