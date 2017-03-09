import os
import sys
import re
import gzip

filename_tbl = 'blast_percent.txt' #sys.argv[1]
filename_tbl2 = 'mart_result.txt' #sys.argv[2]
filename_tbl3 = 'NIBR201605_SuweonTreeFrog109176_tx.combined_nTx_NR_prot6asdasd.fa' #sys.argv[3]

f_dict1 = {}
with open(filename_tbl,"r") as f:
    for line in f:
        list1 = line.split()
        pid = list1[0]
        tid = list1[2]
        align_per = list1[3]
        f_dict1[tid+" "+pid] = [align_per]

'''
f_dict2 = {}
with open(filename_tbl2,"r") as f:
    for i, line in enumerate(f):
        if i % 2 == 0:
            list1 = line.split()
            tid = list1[0]
            pid = list1[1]
            if len(list1) > 2:
                gid = list1[2]
            else : gid = None
        else :
            seq = line
            f_dict2[tid] = [pid, gid, seq]
'''
f_dict2 = {}
with open(filename_tbl2,"r") as f:
    for line in f:
        list1 = line.split()
        if len(list1) > 2:
            tid = list1[0]
            pid = list1[1]
        else : continue

        if len(list1) < 5:
            gid = ""
            seq = list1[3]
        else :
            gid = list1[2]
            seq = list1[4]
        f_dict2[tid+" "+pid] = [gid, seq]

f_dict3 = {}
with open(filename_tbl3,"r") as f:
    for line in f:
        list1 = line.split()
        tid = list1[0][1:]
        position = list1[1]
        f_dict3[tid] = [position]

a=0
with open('test.fa','w') as f_p:
    for tid_pid in f_dict1.keys():
        tid, pid = tid_pid.split()
        if tid_pid in f_dict2 and tid in f_dict3:
            gid = f_dict2[tid_pid][0]
            position = f_dict3[tid][0]
            align_per = f_dict1[tid_pid][0]
            seq = f_dict2[tid_pid][1]
            f_p.write(tid+'\t'+gid+'\t'+align_per+'\t'+position+'\t'+seq+'\n')
            a+=1
print a