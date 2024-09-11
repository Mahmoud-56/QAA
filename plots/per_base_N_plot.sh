#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 4
#SBATCH --mem=8G
#SBATCH --time=1-00:00:00

conda activate QAA 


/usr/bin/time -v python ./per-base-N-plot.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/10_2G_both_S8_L008_R2_001.fastq.gz



