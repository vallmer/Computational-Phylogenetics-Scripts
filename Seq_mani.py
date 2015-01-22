# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 11:30:13 2015

@author: vallmerjordan
"""

# Sequence Manipulation Exercise

# define a DNA sequence (taken from https://github.com/jembrown/CompPhylo_Spr2015/blob/master/CodingSeq.txt)
DNA = "aaaagctatcgggcccataccccaaacatgttggttaaaccccttcctttgctaattaatccttacgctatctccatcattatctccagcttagccctgggaactattactaccctatcaagctaccattgaatgttagcctgaatcggccttgaaattaacactctagcaattattcctctaataactaaaacacctcaccctcgagcaattgaagccgcaactaaatacttcttaacacaagcagcagcatctgccttaattctatttgcaagcacaatgaatgcttgactactaggagaatgagccattaatacccacattagttatattccatctatcctcctctccatcgccctagcgataaaactgggaattgccccctttcacttctgacttcctgaagtcctacaaggattaaccttacaaaccgggttaatcttatcaacatgacaaaaaatcgccccaatagttttacttattcaactatcccaatctgtagaccttaatctaatattattcctcggcttactttctacagttattggcggatgaggaggtattaaccaaacccaaattcgtaaagtcctagcattttcatcaatcgcccacctaggc"

# Print the length of the sequence to the screen
print 'The length of your sequence is', len(DNA), 'bp'
print ' '

# Create and store the RNA equivalent, then print to screen
RNA = DNA.replace('g','G').replace('c','g').replace('G','c').replace('a','u').replace('t','a')
print RNA
print ' '

# Create and store the reverse complement of your sequence, then print to screen.
Comp_DNA = DNA.replace('g','G').replace('c','g').replace('G','c').replace('t','T').replace('a','t').replace('T','a')
print Comp_DNA [::-1]
print ' '

# Extract the bases corresponding to the 13rd and 14th codons from the sequence, then print them to the screen.
codon_13 = DNA[36:39]
print 'codon 13 is', codon_13
print ' '

codon_14 = DNA[39:42]
print 'codon 14 is', codon_14

"""
Create a function to translate the nucleotide sequence to amino acids using the vertebrate mitochondrial genetic code 
(https://github.com/jembrown/CompPhylo_Spr2015/blob/master/VertMitTransTable.txt).
"""
# Make a codon list


list = [] 

# Split Sequence into intervals of 3 bases
for n in range(0, len(DNA), 3): 
# Give definition for a codon
    codon = DNA[n:n+3] 
# add each codon
    list.append(codon) 

# Define and index list of amino acids and corresponding codons
amino_acids = ['F','L','I','M','V','S','P','T','A','Y','H','Q','N','K','D','E','C','W','R','G'] 

codons = [['TTT', 'TTC'],['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],['ATT', 'ATC'],['ATG', 'ATA'],['GTT', 'GTC', 'GTA', 'GTG'],['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],['CCT', 'CCC', 'CCA', 'CCG'],['ACT', 'ACC', 'ACA', 'ACG'],['GCT', 'GCC', 'GCA', 'GCG'],['TAT', 'TAC'],['CAT', 'CAC'],['CAA', 'CAG'],['AAT', 'AAC'],['AAA', 'AAG'],['GAT', 'GAC'],['GAA', 'GAG'],['TGT', 'TGC'],['TGA', 'TGG'],['CGT', 'CGC', 'CGA', 'CGG'],['GGT', 'GGC', 'GGA', 'GGG']] 

#Store length of amino acids
aa_len = len(amino_acids)

#Takes in each codon and returns the corresponding amino acid
def amino(codon):
    for x in range(aa_len): #Each codon
         for z in range(len(codons[x])): # codon list
            if codons[x][z] == codon: 
                return amino_acids[x] #returns the matching amino acid 
            else:
                z = z + 1 #keeps checking list if there is no match

aaSeq = '' #creates an empty string for aa
for i in range(0, len(DNA), 3): #creates the index from 0 to the end of the sequence, with increase of 3
    DNA = DNA.upper()      
    tri = DNA[i:i+3] #defines each triplet in the sequence
    aaSeq = aaSeq + amino(tri) #adds each amino acid to the string.
# Prints the translated sequence to the screen.'''
print 'The corresponding amino acids are:', aaSeq
