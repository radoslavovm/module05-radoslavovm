#!/usr/bin/env python3
# Import Seq, SeqRecord, and SeqIO
from Bio import SeqIO
# Import itertools to take a slice of list
import itertools

#read in paired ILLumina reads from 2 files 
#output results to an interleaved fasta file

leftReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R1.fastq", "fastq")
rightReads = SeqIO.parse("/scratch/AiptasiaMiSeq/fastq/Aip02.R2.fastq", "fastq")

illumina = [] 

#zip iterator
for left, right in zip(leftReads, rightReads):
    #append to list called illumina
    illumina.append(left)
    illumina.append(right)

#outpout
SeqIO.write(illumina, "interleaved.fasta", "fasta")
