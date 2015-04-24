#!/usr/bin/python
import argparse



def get_glycan_sites(seq):
    sites = []
    return sites

def get_binary_sites(seq):
    sites = []
    return sites



def main(indir):
    # for file in indir:
        # for read in file:
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
                        help='The input file path')
    args = parser.parse_args()
    
    indir = args.indir
  
    main(indir)
