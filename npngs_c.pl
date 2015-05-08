#!usr/bin/perl

use strict;
use warnings;

my $fasta_file=shift;

my $fh;
open($fh, $fasta_file) or die "can't open $fasta_file: $!\n";

my %sequence_data;
while (read_fasta_sequence($fh, \%sequence_data)) {
	print "$sequence_data{header}\t";
	my @seq = split('', $sequence_data{seq});
		
	for (my $i = 0; $i <= $#seq-2; $i++){                                             #for 	
                if($seq[$i] eq "N") {				#Scenario where eg N--GT/S 
			if($seq[$i+1] eq "-") {
				my $c = $i+1;
                                my $pos = $i+1;
				until ($seq[$pos] ne "-"){
					$pos++;	
				}
				if (($seq[$pos] ne "P") && (($seq[$pos+1] eq "S") || ($seq[$pos+1] eq "T"))) {
					print "1\t";
				}
				elsif (($seq[$pos] ne "P") && ($seq[$pos+1] eq "-")) {
					my $posn = $pos+1;
                                	until ($seq[$posn] ne "-"){
                                        $posn++;
					}	
					if (($seq[$posn] eq "S") || ($seq[$posn] eq "T")) {
                                        print "1\t";
					}
					else { print "0\t"; }
                                	
				}
				else { print "0\t"; }
					
			}
			elsif (($seq[$i+1] ne "P") && ($seq[$i+2] eq "-")){	#Scenario where eg NG----T/S
				my $pos = $i+2;
                                until ($seq[$pos] ne "-"){
                                        $pos++;
                                }
				if (($seq[$pos] eq "S") || ($seq[$pos] eq "T")){
					print "1\t";
				}
                                else { print "0\t"; }
			}

			elsif (($seq[$i+1] ne "P") && (($seq[$i+2] eq "S") || ($seq[$i+2] eq "T"))){	#Where eg NGS/T
				print "1\t";
			}
			else { print "0\t"; }
		}
		
                else {
                        print "0\t";
                }
	}
print "0\t0\t";



#	print "\n\t";
#	for (my $i = 0; $i <= $#seq; $i++){	
#		print $seq[$i];
#		print "\t";
#
#	}


#print "\n";
#   	print ">$sequence_data{header}\n$sequence_data{seq}\n\n";
print "\n";
}

sub read_fasta_sequence {
   my ($fh, $seq_info) = @_;

   $seq_info->{seq} = undef; # clear out previous sequence

   # put the header into place
   $seq_info->{header} = $seq_info->{next_header} if $seq_info->{next_header};

   my $file_not_empty = 0; 
   while (<$fh>) {
      $file_not_empty = 1;
      next if /^\s*$/;  # skip blank lines
      chomp;    

      if (/^>/) { # fasta header line
         my $h = $_;    
         $h =~ s/^>//;
	 $h =~ s/\r//g;
         if ($seq_info->{header}) {
            $seq_info->{next_header} = $h;
            return $seq_info;   
         }              
         else { # first time through only
            $seq_info->{header} = $h;
         }              
      }         
      else {    
         s/\s+//;  # remove any white space
         $seq_info->{seq} .= $_;
      }         
   }    

   if ($file_not_empty) {
      return $seq_info;
   }    
   else {
      # clean everything up
      $seq_info->{header} = $seq_info->{seq} = $seq_info->{next_header} = undef;

      return;   
   }    
}
