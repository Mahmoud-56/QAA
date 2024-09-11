#!/usr/bin/env python

import gzip
import argparse
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser(description="N score per base distribution")
    parser.add_argument("-f", "--filename", type=str)
    return parser.parse_args()

args = get_args()

total_reads = 0
n_count = {}

with gzip.open(args.filename, 'rt') as f:  # Open gzipped FASTQ file in text mode
        for i, line in enumerate(f):
            if i % 4 == 1:  # Sequence lines (2nd line in every 4 lines)
                total_reads += 1
                line = line.strip()

                for j in range(len(line)):
                    if j not in n_count:
                        n_count[j] = 0  # Initialize all positions in the dict
            
            # Count 'N' at each position
                for j, base in enumerate(line):
                    if base == 'N':
                        n_count[j] += 1 


# Calculate the percentage of 'N' bases at each position
n_percent = []
for pos in range(101):
    count_at_pos = n_count.get(pos)
    percent_at_pos = (count_at_pos / total_reads) * 100
    n_percent.append(percent_at_pos)

# Prepare x (positions) and y (percentages) for plotting
x = list(range(len(n_percent)))
y = n_percent


plt.bar(x, y)
plt.xlabel('Read length (bp)')
plt.ylabel("N content(%)")
plt.title(f"N content across all bases for 10_2G_both_S8_L008_R2")
plt.savefig(f"N_count_distribution_10_2G_both_S8_L008_R2.png")

