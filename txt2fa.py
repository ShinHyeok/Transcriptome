
# coding: utf-8

# In[1]:

import os
import re
import gzip
import sys

filename_tbl = sys.argv[1]
f_tblw = open('%s.fa'%filename_tbl,'w')

with open(filename_tbl,'r') as f:
    for line in f:
        tname = line.split()[0]
        seq = line.split()[-1]
        f_tblw.write('>'+tname+'\n')
        a = 0
        for i in range(len(seq)/60+1):
            tmp_seq = seq[a:a+60]
            a = a+60
            if len(tmp_seq) == 0:
                continue
            if tmp_seq[-1] == '*':
                tmp_seq = tmp_seq[:-1]
            f_tblw.write(tmp_seq+'\n')
f_tblw.close()