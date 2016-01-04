#!/usr/bin/python

import pandas as pd

SEGMENT_FILE = 'CLUC_15kbp_segmented.igv'
GTF_FILE = 'gencode.v19.annotation.gtf'

## Static columns for the platform file
GPL_ID = 'GENCODEv19'
NUM_PROBES  =
ORGANISM    =


copy_numbers = open(SEGMENT_FILE, 'r').read().split()
all_annotation = open(GTF_FILE, 'r').read().split('\n')

gene_annotation = list()



for line in all_annotation:
    if line[0] != '#':
        line = line.split('\t')
        if line[2] == 'gene':
            print line
            # REGION_NAME =
            # CHR         = line[0]
            # START_BP    = line[3]
            # END_BP      = line[4]
            # CYTOBAND    =
            # GENE_SYMBOL =
            # GENE_ID     =

            # GPL_ID, REGION_NAME, CHR, START_BP, END_BP, NUM_PROBES, CYTOBAND, GENE_SYMBOL, GENE_ID, ORGANISM
