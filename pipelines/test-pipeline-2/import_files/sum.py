from sys import argv

count_start = 0
with open(argv[1], "r") as f:
    for line in f.readlines():
        count_start+=int(line)

with open(argv[2], "w") as rw:
    rw.write(str(count_start))