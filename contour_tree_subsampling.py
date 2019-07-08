#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:00:14 2017

@author: gc12847
"""

#alternative tree subsampling algorithm. Define contours eminating out from the root of the reference tree. At each contour, take just one descendant sequence --- ideally, a somewhat average one. Maybe avoids the problem of picking weird taxa because of their long branches.

from Bio import Phylo, AlignIO
from ete3 import Tree
from operator import itemgetter
import os, re
import numpy as np

def get_mean_root_to_tip(tree):
    dists = []
    root = tree.get_tree_root()
    for leaf in tree:
        d = tree.get_distance(root, leaf)
        dists.append(d)
    return np.mean(dists)

def contour_node(root, node, contour): #check whether a node is immediately descendent of a contour  
    if (tree.get_distance(root, node) >= contour) and (tree.get_distance(root, node.up) <= contour):
        #print "TRUE"
        #print node
        #print tree.get_distance(root, node)
        #print tree.get_distance(root, node.up)
        return True
    else:
        return False

def pick_average_tip(node): #given a node, pick the most average of its descendants (in terms of branch length for now...)
    dists = {}
    for leaf in node:
        d = tree.get_distance(node, leaf)
        dists[leaf] = d
    sorted_dists = sorted(dists.items(), key=itemgetter(1))
    middle_node = sorted_dists[int(len(sorted_dists)/2)][0]
    return middle_node

tree = Tree("bac_newick_rooted.txt") #or read in from a file
#print (tree)
mean_root_to_tip = get_mean_root_to_tip(tree)

#divide mean distance into some number of contours
num_contours = 1
contours = []
for i in range(num_contours):
    print (i+2)
    #contours.append(mean_root_to_tip/float(i+2))
    #contours.append(mean_root_to_tip/int(1.5))
    #contours.append(mean_root_to_tip)
    contours.append(mean_root_to_tip*0.6768)
    #contours.append(mean_root_to_tip*0.5)
    #contours.append(mean_root_to_tip*0.6)
    #contours.append(mean_root_to_tip*0.65)
    #contours.append(mean_root_to_tip*0.8)
    
    

print (contours)

#for each contour, print num of nodes for which one descendant will be picked
root = tree.get_tree_root()
for c in contours:
    to_keep = []
    for node in tree.traverse():
        if contour_node(root, node, c):
            node_to_keep = pick_average_tip(node)
            to_keep.append(node_to_keep)
    print ("Contour at " + str(c) + ", " + str(len(to_keep)) + " in total.")
    for taxon in to_keep:
        print (taxon.name)
        
#to write out the alignments
#alignment = AlignIO.read('hug_2016_proteins.txt', "fasta")

#aln_seqs = {} 
#for record in alignment:
 #   aln_seqs[record.id] = str(record.seq)

#outh = open(aln_seqs + "_reduced.fasta", "w")
#for tip in taxa:
 #   outh.write(">" + str(tip.name) + "\n" + str(aln_seqs[tip.name]) + "\n")
#outh.close()       











