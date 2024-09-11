import gzip
import argparse
import bioinfo
import matplotlib.pyplot as plt

def get_args():
    parser = argparse.ArgumentParser(description="Quality score per base distribution")
    parser.add_argument("-s", "--list_size", type=int)
    parser.add_argument("-f", "--filename", type=str)
    parser.add_argument("-n", "--name", help="Name of the file for naming the plot", type=str)
    return parser.parse_args()

args = get_args()

def init_list(size, value=0.0):
    return [value] * size

my_list = init_list(args.list_size)
num_lines = 0

# Open the gzip file and read it line by line
with gzip.open(args.filename, 'rt') as f:  # 'rt' mode is for reading text
    for i, line in enumerate(f):
        if i % 4 == 3:  # Only process the quality score lines
            num_lines += 1
            newline = line.strip()
            for j, ch in enumerate(newline):
                qual_score = bioinfo.convert_phred(ch)
                my_list[j] += qual_score

N = num_lines
for i, summ in enumerate(my_list):
    avg_score = summ / N
    my_list[i] = avg_score 

x_values = range(len(my_list))
plt.bar(x_values, my_list)
plt.xlabel('Base pair')
plt.ylabel('Average quality score')
plt.title(f"Quality score distribution for {args.name}")
plt.savefig(f"quality_score_distribution_{args.name}.png")
