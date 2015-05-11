#!/usr/bin/python
import argparse
import re

from Bio import SeqIO


def get_glycan_sites(seq):
    seq = seq.replace("-", "")
    sites = []
    p = re.compile('N[^P][TS]')
    iterator = p.finditer(seq)
    for match in iterator:
        start, end = match.span()
        sites.append(start)
    return sites

def get_binary_sites(seq):
    sites = []
    p = re.compile('N[^P][TS]')
    iterator = p.finditer(seq)
    for match in iterator:
        start, end = match.span()
        sites.append(start)
    sites_seq = ""
    for i in range(len(seq)):
        if i in sites:
            sites_seq += "1"
        else:
            sites_seq += "0"

    return sites_seq


def main(infile):
    handle = open(infile, "rU")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    for record in records:
        sites = get_glycan_sites(str(record.seq))
        binary_sites = get_binary_sites(str(record.seq))

        # print binary_sites
        # get binary sites (read)
        # write that to file
        # append it to data structure
    # make summary of data
    # write summary to file

    # make plots of summary.    
    
    
    print "end"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Glycan binding site detection.')
    parser.add_argument('-in', '--infile', type=str,
                        help='The input path to the source file', required = True)
    args = parser.parse_args()
    
    infile = args.infile

    main(infile)
