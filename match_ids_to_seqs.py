#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:04:14 2017

@author: gc12847
"""
import sys

mcl_file = sys.argv[1] #MCL output
seqfile = sys.argv[2] #File with all original sequences

f = open ('mcl_file', 'r')
from Bio import SeqIO
#seqs = SeqIO.index('seqfile', 'fasta') #seq is a dictionary, key = record IDs, values = records
seqs = {}
for seq_record in SeqIO.parse(seqfile,'fasta'):
    seqs[seq_record.id] = seq_record    
i = 0
idList = {}
for line in f:
    lst = line.split()
    idList = lst
    writefile = open("Output_%i" %i, 'w')
    for a in idList:
        if a in seqs:
            SeqIO.write(seqs[a],writefile, "fasta")
        #for seq_record in SeqIO.parse('ALLseqs.fas', 'fasta'):
         #   if seq_record.id == a:
                #print (seq_record.id)
          #      SeqIO.write(seq_record,writefile, "fasta")
                #print(len(seq_record))
    i+=1
