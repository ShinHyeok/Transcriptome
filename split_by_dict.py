import os
import sys
import re
import gzip

filename_tbl = sys.argv[1]
filename_tbl2 = sys.argv[2]

def diction(name):
    f = open(name,'r')
    table = []
    for line in f:
        table.append(line)
    return table

f_tbl = diction(filename_tbl)
f_tbl2 = diction(filename_tbl2)
f_p = open('mart_result.txt','w')

for line in f_tbl:
	Pname = line.split()[2]
	Tid = line.split()[3]
	for line in f_tbl2:
		Gname = line.split()[0]
		Pname2 = line.split()[1]
		Tname = line.split()[2]
		Seq = line.split()[3]
		if Pname == Pname2:
			f_p.write(Tname + '\t' + Pname + '\t' + Tid + '\t' + Gname + '\t' + Seq + '\n')

f_tbl.close()
f_tbl2.close()
f_p.close()
