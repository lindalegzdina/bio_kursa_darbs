#!/usr/bin/env python3
import pandas as pd
import sys

if __name__ == "__main__":
    merged_data = pd.read_table(sys.argv[2])
    for fname in sys.argv[3:]:
        read_counts = pd.read_table(fname)
        keyname = read_counts.columns[0]
        merged_data = pd.merge(merged_data,read_counts, on=keyname, how="outer")
    merged_data.fillna(0, inplace=True)
    merged_data.to_csv(sys.argv[1], sep="\t", index=False)
