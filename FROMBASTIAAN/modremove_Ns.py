#!/usr/bin/env python3

import os, sys


def main():
    if len(sys.argv) != 4:
        sys.exit('Please provide input file and output file (in that order!!):)')

    fold = sys.argv[1]
    fExt = str(sys.argv[2])
    out_fold = sys.argv[3]
    d = {}

    # if file == out_file:
    #     sys.exit('input file and output_file are the same!!')
    FL=os.listdir(fold)
    for file in FL:

        if file.rstrip().endswith(fExt):
            with open(file, 'r') as f:
                for line in f:
                    line = line.rstrip()

                    if line.startswith('>'):
                        header = line

                        d[header] = ''
                    else:
                        seq = line

                        d[header] += seq

            out_file=out_fold+file
            with open(out_file, 'w') as outf:
                for contig in sorted(d):
                    if set(d[contig]) == set('N'):
                        continue

                    outf.write('{0}\n{1}\n'.format(contig, d[contig]))

        d = {}

if __name__ == '__main__':
    main()
