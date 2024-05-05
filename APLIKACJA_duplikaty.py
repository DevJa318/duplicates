#!/usr/bin/env python

"""
Print all duplicate file from given file containing file paths
It works with files that are the same but having different names.

This program was used to work with linux shell promt. 

INPUT:
FILE_LIST - file with list of locations of all files to check.
	Meant to use with bash find command
	ie. for all files within directory and directory2  do:
	find /home/devja318/Dokumenty/STARSZE_PROGRAMY/PROG_MOJE/Duplikaty/duplikaty_test/ -type f > ~/allfiles.txt
	find ./directory2 -type f >> ~/allfiles.txt

OUTPUT - print hash of the file following by path to the same files
"""
import hashlib


FILE_LIST = '/home/devja318/Dokumenty/STARSZE_PROGRAMY/PROG_MOJE/Duplikaty/allfiles.txt'

def hashfile(file: str, block_size: int = 65536) -> str:
    """Generate the hash of any file according to the sha256 algorithm."""
    with open(file, 'rb') as message:
        m = hashlib.sha256()
        block = message.read(block_size)
        while len(block) > 0:
            m.update(block)
            block = message.read(block_size)
        digest = m.hexdigest()

    return digest

all_digests = []
with open(FILE_LIST,'r') as f:
    for file_path in f:
        file_digest = hashfile(file_path.strip('\n'))
        all_digests.append((file_digest, file_path))
        
sorted_digets = sorted(all_digests)

current_hash = (0,0)
previous_hash = sorted_digets[0]

for file in sorted_digets:
    if file[0] != current_hash[0]:
        print(file[0])
        print('\t' + file[1])
        current_hash = file
    elif file[0] == previous_hash[0]:
        print('\t', file[1])
    previous_hash = file
