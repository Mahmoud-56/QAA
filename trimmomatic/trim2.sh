#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 1
#SBATCH --time=0-3

conda activate QAA


/usr/bin/time -v trimmomatic PE -phred33 /projects/bgmp/malm/bioinfo/Bi623/FastQC/cutadapt_adapter_trim/trimmed_10_2G_both_S8_L008_R1_001.fastq.gz \
 /projects/bgmp/malm/bioinfo/Bi623/FastQC/cutadapt_adapter_trim/trimmed_10_2G_both_S8_L008_R2_001.fastq.gz \
 out_paired_10_2G_both_S8_L008_R1_001.fastq.gz \
 out_unpaired_10_2G_both_S8_L008_R1_001.fastq.gz \
 out_paired_10_2G_both_S8_L008_R2_001.fastq.gz \
 out_unpaired_10_2G_both_S8_L008_R2_001.fastq.gz \
 ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35

#TruSeq3-PE.fa.... Remove Illumina adapters provided in the TruSeq3-PE.fa file (provided). Initially 
#Trimmomatic will look for seed matches (16 bases) allowing maximally 2
#mismatches. These seeds will be extended and clipped if in the case of paired end
#reads a score of 30 is reached (about 50 bases), or in the case of single ended reads a
#score of 10, (about 17 bases).
 