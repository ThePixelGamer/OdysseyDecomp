# Renames functions in an IDA database to match the function names
# in the decompiled source code.

import csv
import idc
import os

csv_path = os.path.join(os.path.dirname(__file__), "../data/odyssey_functions.csv")

with open(csv_path, "r") as f:
    reader = csv.reader(f)
    # Skip headers
    next(reader)
    for fn in reader:
        addr = int(fn[0], 16)
        name = fn[3]
        if name and fn[1] != "L":
            idc.set_name(addr, name)