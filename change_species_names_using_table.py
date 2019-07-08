#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 14:47:03 2017

@author: gc12847
"""
import csv, re, os
from ete3 import PhyloTree
from Bio import SeqIO

table_used = sys.argv[1] #Table with original names and names to replace
reader = csv.reader(open(table_used, 'r'))
file_to_species = {}
for row in reader:
   k, v = row
   file_to_species[v] = k

protein_to_file = {}
 
 #loop over the protein files and create a dictionary where the keys are protein sequence headers and the values are the file they are in
protein_files = [file for file in os.listdir(".") if file.endswith(".faa")] 
for file in protein_files:
    sequences = SeqIO.parse(file, "fasta")
    for record in sequences:
        header = record.description
        fields = re.split(" ", header)
        identifier = fields[0]
        identifier = identifier.replace(".", "-").replace("_", "-")
        protein_to_file[identifier] = file

import glob

#loop through all lines in all files and replace names with correct names form library file_to_species - many of these were specific to my dataset
file_paths = sys.argv[2] #.phy files to change
files = glob.glob(file_paths)
for file in files:
    bootstrapped_trees = []
    outfile = file + "_renamed"
    f = open(file)
    for line in iter(f):
       t = PhyloTree(line)
       for n in t.get_leaves():
           fields = re.split('_', n.name)
           lookup_id = ''
           if len(fields) == 1: #for cases which don't follow the normal pattern.
               field5 = re.split("-", fields[0])
               lookup_id = field5[0] + "-" + field5[1]
           elif len(fields) > 1: #for most cases
                fieldz = re.split("-", fields[1])
                if len(fieldz) == 1: #cover the odd cases of e.g. Ga000dfs_01234
                    lookup_id = fields[0] + "-" + fieldz[0]
                elif fieldz[1] == 'WP':
                    lookup_id = fieldz[1] + "-" + fieldz[2] + '-' + fieldz[3]
                elif len(fieldz[0]) == 2:
                    lookup_id = fieldz[0] + "-" + fieldz[1] + "-" + fieldz[2] 
                elif len(fieldz[0]) == 10:
                    lookup_id = fieldz[0]
                else:
                    lookup_id = fieldz[0] + "-" + fieldz[1]
    
           containing_file = protein_to_file[lookup_id]
           species_name = file_to_species[containing_file]
    
           # print(lookup_id)
           # print(containing_file)
           # print(species_name)
           if len(fields) == 1:
               n.name = species_name + "_" + fields[0]
           else:
               n.name = species_name + "_" + fields[1]
           # print (n.name)
       bootstrapped_trees.append(t)
           #print (t)
           #outfilez = file + "_renamed"
           
    outh = open(outfile, "w") 
    for tree in bootstrapped_trees:
        outh.write(tree.write() + "\n") 
    outh.close()
          # t.write(format=1, outfile=outfilez)   
    #f.close()
              

     
