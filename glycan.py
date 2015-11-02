#!/usr/bin/python
import argparse
import re
import os

from daves_tools import fasta_to_dct


def get_glycan_sites(seq, regex_pattern):
    seq = seq.replace("-", "")
    sites = []
    p = re.compile(regex_pattern)
    iterator = p.finditer(seq)
    for match in iterator:
        start, end = match.span()
        sites.append(start)
    return sites

def get_binary_sites(seq, regex_pattern):
    sites = []
    p = re.compile(regex_pattern)
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

def main(infile, out_dir):
    records = fasta_to_dct(infile)
    in_dir, in_fn = os.path.split(infile)[0], os.path.split(infile)[1]

    gly_fn = out_dir + in_fn[:in_fn.rfind(".")] + "_glycans_pos.out"
    bin_fn = out_dir + in_fn[:in_fn.rfind(".")] + "_glycans_binary.out"

    gly_fw = open(gly_fn, "w")
    bin_fw = open(bin_fn, "w")

    regex_pattern = 'N[\-]*[^P\-][\-]*[TS]'

    summary_gly_pos = []
    summary_binary = []

    for key, seq in records.items():
        sites = get_glycan_sites(seq, regex_pattern)
        binary_sites = get_binary_sites(seq, regex_pattern)

        gly_fw.write(">"+key+"\n"+str(sites)+"\n")
        bin_fw.write(">"+key+"\n"+str(binary_sites)+"\n")

        if len(sites) > 1:
            summary_gly_pos.append(sites)
            summary_binary.append(binary_sites)

    gly_fw.close()
    bin_fw.close()
    
    print "end"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Glycan binding site detection.')
    parser.add_argument('-in', '--infile', type=str,
                        help='The input path to the source file', required = True)
    parser.add_argument('-out', '--outdir', type=str,
                        help='The path to the output', required = True)
    args = parser.parse_args()
    
    infile = args.infile
    outdir = args.outdir

    main(infile, outdir)
