#!/usr/bin/python
import argparse
import os
from Bio import SeqIO

def get_glycan_sites(seq):
    sites = []
    return sites

def get_binary_sites(seq):
    sites = []
    return sites


def main(indir, ft):
    file_list = os.walk(indir).next()[2]
    file_list = [f for f in file_list if f[-(len(ft)):] == ft]
    for fn in file_list:
        print indir + fn
        handle = open(indir + fn, "rU")
        records = list(SeqIO.parse(handle, "fasta"))
        handle.close()
        for record in records:
            binary_sites = get_binary_sites(str(record.seq))
            print binary_sites
            # get binary sites (read)
            # write that to file
            # append it to data structure
    # make summary of data
    # write summary to file

    # make plots of summary.    
    
    
    print "end"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Glycan binding site detection.')
    parser.add_argument('-in', '--indir', type=str,
                        help='The input file path', required = True)
    parser.add_argument('-ft', '--filetype', type=str, 
            help="The file extension (without a full stop) of the files to be used, which are located in the specified input directory.", 
            required=True)
    args = parser.parse_args()
    
    indir = args.indir
    ft = args.filetype
  
    main(indir, ft)
