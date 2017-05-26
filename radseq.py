import re
import matplotlib.pyplot as plt 
import sys

name = 'Xenopus_tropicalis_v9.1_genomic.fna'
save = 'genome'
f_enz= open('regular_enz.txt','r')

enzyme = {}

for line in f_enz:
    if len(line.strip())<2:
        continue
    enz = line.split()[0]
    cut = line.split()[1]
    enzyme[enz]=cut
        
f_genome = open(name,'r')

genome = ''
for line in f_genome:
    if line.startswith('>'):
        continue
    else:
        genome += line.strip()
enz_list = enzyme.keys()

cut = {}
for enz in enz_list:
    tmp_enz = enzyme[enz]
    pattern = tmp_enz[:tmp_enz.find('/')]+tmp_enz[tmp_enz.find('/')+1:]
    list1 = [m.start()+tmp_enz.find('/') for m in re.finditer(pattern, genome.upper())]
    cut[enz] = list1
enz_list = enzyme.keys()

for key in cut.keys():
    for key2 in cut.keys():
        length = []
        num = 0
        coverage = 0
        if key == key2:
            break
        list_s = cut[key]+cut[key2]
        a = set(list_s)
        comp_set = sorted(a,reverse=True)
        for i in range(len(comp_set)-1):
            tmp_len = comp_set[i]-comp_set[i+1]
            length.append()
            if tmp_len >100 and tmp_len <500:
                num += 1
                coverage += 1
        plt.hist(length, rwidth=0.8)
        plt.title(key +' with '+key2 +'\n' + str(float(coverage)/len(genome))+' with '+'num')
        plt.suptitle(title_string, y=1.05, fontsize=17)
        plt.savefig('%s/%s + %s.png'%(save,key,key2))
        plt.close()
f_genome.close()
f_enz.close()
