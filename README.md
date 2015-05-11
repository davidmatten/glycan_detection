# glycan_detection
glycan_detection

## Description
This tool is used to detect N-linked glycosylation in amino acid sequences.


###### Tool input:
<ol>
<li>
-in \path\to\fasta_file.fasta
</li>
</ol>

###### Tool output:
In the same directory as the input file, two files will be created.
<ol>
<li>fasta like output of positions at which the glycosylation sites are found (if any are).
  <br>example outfile:<br>
  <pre><code>
  > seq1<br>
  1, 45, 67<br>
  > seq2<br>
  33, 36, 90<br>
  </code></pre>
</li>
<li>fasta like output. Binary version.
  Each sequence position is represented by a character; either a one, or a zero.
  A zero indicates that this site is not the starting position for a glycosylation site.
  A one indicates that this site is a starting position for a glycosylation site.
  <br>example outfile:<br>
  <pre><code>
  > seq1<br>
  0100<br>
  > seq2<br>
  0000<br>
  </code></pre>
</li>
</ol>
<br><br><br><br>
#### SPECIAL NOTES
Strips ALL gaps out of sequences. Any output positions given will be without gaps.