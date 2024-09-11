#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 1
#SBATCH --time=0-3

conda activate QAA


/usr/bin/time -v python ./sam_parsing.py -f alignment_output_10_2G_both_S8_L008Aligned.out.sam 