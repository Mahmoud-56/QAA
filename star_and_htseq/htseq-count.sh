#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 1
#SBATCH --time=1-00:00:00

conda activate QAA


/usr/bin/time -v htseq-count --stranded=yes alignment_output_10_2G_both_S8_L008Aligned.out.sam ../Mus_musculus.GRCm39.112.gtf > htseq_count_stranded_10_2G_both_S8_L008.out

/usr/bin/time -v htseq-count --stranded=reverse alignment_output_10_2G_both_S8_L008Aligned.out.sam ../Mus_musculus.GRCm39.112.gtf > htseq_count_reverse_10_2G_both_S8_L008.out

