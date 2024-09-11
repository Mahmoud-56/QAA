#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 4
#SBATCH --mem=8G
#SBATCH --time=0-3




conda activate bgmp-velvet


/usr/bin/time -v python ./mean_qscore_plots.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/31_4F_fox_S22_L008_R1_001.fastq.gz -s 101 -n 31_4F_fox_S22_L008_R1_001


/usr/bin/time -v python ./mean_qscore_plots.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/31_4F_fox_S22_L008_R2_001.fastq.gz -s 101 -n 31_4F_fox_S22_L008_R2_001

/usr/bin/time -v python ./mean_qscore_plots.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/10_2G_both_S8_L008_R1_001.fastq.gz -s 101 -n 10_2G_both_S8_L008_R1_001

/usr/bin/time -v python ./mean_qscore_plots.py -f /projects/bgmp/shared/2017_sequencing/demultiplexed/10_2G_both_S8_L008_R2_001.fastq.gz -s 101 -n 10_2G_both_S8_L008_R2_001