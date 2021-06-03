#!/usr/bin/env python3
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio import SeqIO
import sys
# fname="results/fastq_raw/IonXpress_077_rawlib.basecaller/IonXpress_077_rawlib.basecaller.fastq"
fname=sys.argv[1]
outname=sys.argv[2]
for seq_record in SeqIO.parse(fname, "fastq"):
        print(seq_record.id)
revcom_fq = [rec.reverse_complement(id="rc_"+rec.id,description="") for rec in SeqIO.parse(fname, "fastq")]
SeqIO.write(revcom_fq, outname, "fastq")
