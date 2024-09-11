#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 1
#SBATCH --time=0-3

conda activate QAA

/usr/bin/time -v ../fastqc /projects/bgmp/malm/bioinfo/Bi623/FastQC/trimmomatic/out_paired_10_2G_both_S8_L008_R1_001.fastq.gz /projects/bgmp/malm/bioinfo/Bi623/FastQC/trimmomatic/out_paired_10_2G_both_S8_L008_R2_001.fastq.gz
