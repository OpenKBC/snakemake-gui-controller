from sys import argv
import pandas as pd

count_start = 0
with open(argv[1], "r") as f:
    data = f.read()
with open(argv[2], "w") as rw:
    rw.write(data+("-this is test result"))