#!/usr/bin/python3

'''
Title: GC-plot heat map
Date: 2017-01
Author: Vanja Börjesson 

Description:
	This is a program that calculates the CG-content over several sequences. 

Procedure:
	This program takes an fasta file as input and calculates the GC frequency in a window that is
        specified by the user and slides over the sequence be step length that is also specified by
        the user. The GC frequency for each window in that sequence is saved into a list. This is repeated
        for att sequences in the in file. The lists are saved as csv files and returned into current working
        directory.
        The length of every sequence and the total CG frequence is calculated and saved into a second csv
        file and is also returned into current working directory.
 
	
Usage:
	./BlastParser.py window_size step in.fasta out.csv out.csv


'''

import argparse

usage = '''This program counts the CG content over one or more sequences and plots the results as a heat map.''' 

parser = argparse.ArgumentParser(description=usage)

parser.add_argument(
	'-n', 
	metavar='WINDOW SIZE',
	dest='window_size',
	help = 'number of nucleotides that should be included in the window',
	type=int,
	required= True
	)

parser.add_argument(
	'-m', 
	metavar='STEP SIZE',
	dest='step_size',
	help = 'number of steps for the window that will be calculated',
	type=int, 
	required= True
	)
	
parser.add_argument(
	'-i',
	metavar = 'INFILE',
	dest='infile',
	help= 'one or several sequences in fasta',
	#type=argparse.FileType('r'),
	required= True
	)

parser.add_argument(
	'-o',
	metavar = 'OUTFILE FREQUENCE',
	dest='outfile_freq',
	help='CG-content file (.csv)',
	#type=argparse.FileType('w'),
	required= True
	)

parser.add_argument(
	'-p',
	metavar = 'OUTFILE INFO',
	dest='outfile_info',
	help='Information file (.csv)',
	#type=argparse.FileType('w'),
	required= True
	)
	
args = parser.parse_args()



########## The script starts here ###################

GC_count = []
GC_count_tot = []
seq = []
ids = []
window = args.window_size 
step = args.step_size
in_fasta = args.infile
out_freq = args.outfile_freq
out_info = args.outfile_info
counter = 0
string = ''
seq_length = []

with open (in_fasta, 'r') as f_in:
	for line in f_in:
		line = line.strip().upper()

		# Save the IDs and append sequences to list 
		if line.startswith('>'):	
			seq.append(string)
			line = line.split()
			print(line[0][1:])
			seq.append(line[0][1:])
			ids.append(line[0][1:]) 
			string = ''
					
		# Save the sequence into a list of nucleotides 
		else:
			string += line
				
	# For the last sequence
	seq.append(string)
	seq = seq[1:]

# Calculate the average CG-content in a specific window size for all sequences
# save the results in a list CG_count
for a in range(1, len(seq), 2):
	GC_count_1seq = []
	for i in range(window-1, len(seq[a])-1, step):
		wind = []
		wind.append(seq[a][i-window: i]) 
		GC_count_1seq.append(sum(wind[0].count(x) for x in ('C','G'))/window)
	
	GC_count.append(GC_count_1seq[1:])	
	
	# calculate the total GC-content
	GC_count_tot.append(sum(seq[a].count(x) for x in ('C','G'))/len(seq[a]))
	
	#calculate the total sequence length
	seq_length.append(len(seq[a]))
	
	
# control that the number of ids are the same as sequences 
if len(ids) != len(GC_count): 
	print('Error, the number of ids does not match the number of sequences') # can I break somehow?	

import csv
from itertools import zip_longest

# save GC-cont into a csv-file
with open(out_freq, 'w') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow([*ids])
    rows=zip_longest(*GC_count)
    for row in rows:
    	writer.writerow(row)
  
# save inforations into another csv-file
masterlist = [ids, seq_length, GC_count_tot]
with open(out_info, 'w') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    rows=zip(*masterlist)
    for row in rows:
    	writer.writerow(row) 	
    	
   	   	  









