#!/usr/bin/env python 
import argparse


def get_args():
    parser = argparse.ArgumentParser(description="Counting mapped and Unmapped reads in sam file")
    parser.add_argument("-f", "--filename", type=str)
    return parser.parse_args()

args = get_args()



mappedcount = 0
unmappedcount = 0 
with open(args.filename,"r") as fh:
    for line in fh:
        if line.startswith("@"):
            continue
        field = line.split('\t')
        bitflag = int(field[1])
        if((bitflag & 4) != 4) and ((bitflag & 256)!= 256): #mapped is true and secondary alignment is false
            mapped = True
            mappedcount += 1
        elif ((bitflag & 256)!= 256): #mapped is false and secondary alignment is false 
            unmappedcount += 1

print(f"The number of mapped reads is {mappedcount}")
print(f"The number of unmapped reads is {unmappedcount}")