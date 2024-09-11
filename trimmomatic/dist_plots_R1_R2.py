#!/usr/bin/env python 

import matplotlib.pyplot as plt
import argparse
import gzip
import numpy as np


def get_args():
    parser = argparse.ArgumentParser(description="Read Length Distribution Plot AFter Trimming Between R1 and R2")
    parser.add_argument("-f1", "--filename1", help="What is the file name", type=str)
    parser.add_argument("-f2", "--filename2", help="What is the file name", type=str)
    return parser.parse_args()

args = get_args()

def count_read_length(file):
    count_dict = {} 
    with gzip.open(file) as fh: 
        for i, line in enumerate(fh):
            if i % 4 == 1:
                line_length = len(line.strip())
                if line_length in count_dict:
                    count_dict[line_length] += 1

                else:
                    count_dict[line_length] = 1

    return count_dict



count_dict1 = count_read_length(args.filename1)
count_dict2 = count_read_length(args.filename2)

x1 = [] 
y1 = [] 

for length, count in sorted(count_dict1.items()):
    x1.append(length)
    y1.append(count)

x2 = []
y2 = []
for length, count in sorted(count_dict2.items()):
    x2.append(length)
    y2.append(count)

# Convert lists to numpy arrays for to shift bars when plotting 
x1 = np.array(x1)
y1 = np.array(y1)
x2 = np.array(x2)
y2 = np.array(y2)


plt.bar(x1, y1, label="R1", color="black", alpha = 0.5)  
plt.bar(x2, y2, label="R2", color="red", alpha = 0.5)

plt.xlabel("Read Length")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.title("Read Length Distribution For 10_2G_both_S8_L008 Between R1 and R2 After Trimming", loc='center', wrap=True)
plt.savefig("10_2G_both_S8_L008.png")

