import argparse
import csv

def main():
    parser = argparse.ArgumentParser(
        description='Read in a file or set of files, and return the combined file.')
    parser.add_argument('filepaths', nargs='+', help='Path of a file')
    parser.add_argument('--output', default='combined.csv', help='Output filename')
    args = parser.parse_args()

    # Parse files
    samples_data = []
    for filename in args.filepaths:
        with open(filename, "r") as f:
            data = dict()
            input = f.readlines()
            for line in input:
                res = [x.strip() for x in line.split("\t")]
                if res[0] != "":#
                    data[res[0]] = res[1]
            samples_data.append(data)
    
    # Create a header for a row:
    row_headers = set()
    for sample in samples_data:
        for peptide_name in data.keys():
            row_headers.add(peptide_name)
    
    # Count peptides, prepare data for Output
    output_data = []
    for peptide_name in row_headers:
        counts = [data.get(peptide_name, 0) for data in samples_data]
        row = [peptide_name] + counts
        output_data.append(row)

    # Create output result
    with open(args.output, 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(["Peptide"] + args.filepaths)
        for row in output_data:
            w.writerow(row)

if __name__ == '__main__':
    main()
