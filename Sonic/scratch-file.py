import os

dir = '**directory**'
directory = os.fsencode(dir)
ncs = []

for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".mid"): 
         nc = music_corpus (filename)
         ncs += nc
     else:
         continue

list(set(ncs)).sort()

import csv

# save the file into a CSV just in case (pkl would be overkill, json not needed = flat/unstructured)

with open('BoN', 'w', newline='') as myfile: # BoN = Bag of Notes
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(ncs)

# [0] = rest

ItN = dict(enumerate(ncs, start=1)) # index-to-note
NtI = dict((v,k) for k,v in ItN.items()) # note-to-index
