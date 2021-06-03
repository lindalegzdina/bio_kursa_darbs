#!/usr/bin/env python3
from Bio import SeqIO
from collections import Counter
from Bio.Seq import Seq
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re

def fragment_sequence(s,ws):
    seqs=[]
    for i in range(0,len(s)-ws):
        j=i+ws
        seqs.append(Seq(s[i:j]))
    return seqs

# fname = "results/template_filtered_fq/D10C9_S25.extendedFrags/D10C9_S25.extendedFrags.rest.fastq"
# aa = aas[1]
def strip_aa(aa):
    stripped_aa = re.sub('\*.*','*',str(aa))
    res = Seq(stripped_aa, aa.alphabet)
    return res

def write_kmer_table(fname,outname):

    fq = [rec for rec in SeqIO.parse(fname,"fastq")]
    aas = [rec.seq.translate() for rec in fq if len(rec.seq.translate())]
    stripped_aas = [strip_aa(x) for x in aas]
    kmer_freq = Counter([str(x) for x in stripped_aas])
    kmer_freq_recs = []
    for k in sorted(kmer_freq, key=kmer_freq.__getitem__,reverse=True):
        kmer_freq_recs.append(tuple((k,kmer_freq[k])))

    kmer_freq_table = pd.DataFrame.from_records(kmer_freq_recs,columns=["kmer","count"])
    kmer_freq_table.to_csv(outname,sep="\t",index=False, header=False)
    return

# fname="results/template_filtered_fq/IonXpress_077_rawlib.basecaller/IonXpress_077_rawlib.basecaller.rest.fastq"
if __name__ == "__main__":
    fname=sys.argv[1]
    outname=sys.argv[2]
    write_kmer_table(fname,outname)

