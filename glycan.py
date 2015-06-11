#!/usr/bin/python
import argparse
import re

from daves_tools import fasta_to_dct


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
    records = fasta_to_dct(infile)

    gly_fn = infile[:infile.rfind(".")] + "_glycans_pos.out"
    gly_fw = open(gly_fn, "w")
    bin_fn = infile[:infile.rfind(".")] + "_glycans_binary.out"
    bin_fw = open(bin_fn, "w")

    summary_gly_pos = []
    summary_binary = []
    seq_has_glyc = 0

    for key, seq in records.items():
        sites = get_glycan_sites(seq)
        binary_sites = get_binary_sites(seq)

        gly_fw.write(">"+key+"\n"+str(sites)+"\n")
        bin_fw.write(">"+key+"\n"+str(binary_sites)+"\n")

        if len(sites) > 1:
            seq_has_glyc += 1
        summary_gly_pos.append(sites)
        summary_binary.append(binary_sites)

    total_sites = sum([len(x) for x in summary_gly_pos])

    #print "A total of %s sites were found in %s sequences." %(total_sites, seq_has_glyc)

    gly_fw.close()
    bin_fw.close()
    
    print "end"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Glycan binding site detection.')
    parser.add_argument('-in', '--infile', type=str,
                        help='The input path to the source file', required = True)
    args = parser.parse_args()
    
    infile = args.infile

    main(infile)
