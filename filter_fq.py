#!/usr/bin/env python3
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio import SeqIO
import sys
fname=sys.argv[1]
outname=sys.argv[2]
filtered_fq = []
for rec in SeqIO.parse(fname,"fastq"):
    if (str(rec[0:3].seq)=="TAC") and (str(rec[-3:].seq)=="TAA"):
        filtered_fq.append(rec)
SeqIO.write(filtered_fq, outname, "fastq")
