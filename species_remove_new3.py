#Script to remove species from sequence files

import fileinput
import glob
from itertools import islice
from Bio import SeqIO
import sys

list_file = sys.argv[1] #List of species to keep
lis = open (list_file).readlines()
#print(lis)

file_paths = sys.argv[2] #Sequence files 
i=0
files = glob.glob(file_paths)
for file in files:
	file_sequences = SeqIO.index(file, "fasta")
	writefile = open("out_%i.fa" %i, 'w')
	for species_name in lis:
		if species_name.rstrip() in file_sequences:
			writefile.write(">" + species_name + str(file_sequences[species_name.rstrip()].seq) + "\n")
		i+=1
	writefile.close()
