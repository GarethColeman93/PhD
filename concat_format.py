#Script to reformat names in fasta alignment files for concatenation

import fileinput
import glob
import sys

file_paths = sys.argv[1]
files = glob.glob(file_paths)
for file in files:
	with fileinput.FileInput(file, inplace=True, backup='.backup') as file:
		for line in file:
			if line.startswith('>'):
				if ']' in line:
					line = line.replace(']', '')
					lst = line.split('[')
					if '[00-' in line:
						print('>', lst[1], end='', sep='')
					else:
						print('>', lst[2], end='', sep='')
			else:
				print(line, sep='', end='')
		
