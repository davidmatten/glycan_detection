# glycan_detection
glycan_detection

## Description
This tool is used to detect N-linked glycosylation in amino acid sequences.

###### Tool input:
1. -in \path\to\fasta_file.fasta

###### Tool output:

In the same directory as the input file, two files will be created.

1. fasta like output of positions at which the glycosylation sites are found (if any are).

    ```
    Code
    More Code
    ```
2. blaa

  example outfile:
    ~~~~
    > seq1
    1, 45, 67
    > seq2
    33, 36, 90
    ~~~~

2. fasta like output. Binary version.
  Each sequence position is represented by a character; either a one, or a zero.
  A zero indicates that this site is not the starting position for a glycosylation site.
  A one indicates that this site is a starting position for a glycosylation site.

  example outfile:

```
#!python

  > seq1
  0100
  > seq2
  0000
```


#### SPECIAL NOTES
Strips ALL gaps out of sequences. Any output positions given will be without gaps.