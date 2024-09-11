#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 1


conda activate QAA


#/usr/bin/time -v python ./dist_plots.py -f1 out_paired_31_4F_fox_S22_L008_R1_001.fastq.gz -f2 out_paired_31_4F_fox_S22_L008_R2_001.fastq.gz



/usr/bin/time -v python ./dist_plots.py -f1 out_paired_10_2G_both_S8_L008_R1_001.fastq.gz -f2 out_paired_10_2G_both_S8_L008_R2_001.fastq.gz