#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) != 3:
        sys.exit('Please provide input file and output file (in that order!!):)')

    file = sys.argv[1]
    out_file = sys.argv[2]

    if file == out_file:
        sys.exit('input file and output_file are the same!!')

    d = {}

    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()

            if line.startswith('>'):
                header = line

                d[header] = ''
            else:
                seq = line

                d[header] += seq
                
    with open(out_file, 'w') as outf:
        for contig in sorted(d):
            if set(d[contig]) == set('N'):
                continue

            outf.write('{0}\n{1}\n'.format(contig, d[contig]))


if __name__ == '__main__':
    main()
