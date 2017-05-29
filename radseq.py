import re
import matplotlib.pyplot as plt 
import sys

name = sys.argv[1]
save = sys.argv[2]
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
print 'done'
cut = {}
for enz in enz_list:
    tmp_enz = enzyme[enz]
    pattern = tmp_enz[:tmp_enz.find('/')]+tmp_enz[tmp_enz.find('/')+1:]
    list1 = [m.start()+tmp_enz.find('/') for m in re.finditer(pattern, genome.upper())]
    cut[enz] = list1
enz_list = enzyme.keys()
print 'done2'

tmp_coverage = 0
candidate = ''
cndidate_num = ''
count = 0

keysave = {}
for key in cut.keys():
    for key2 in cut.keys():
        length = []
        num = 0
        coverage = 0
        if key == key2:
            continue
        list_s = cut[key]+cut[key2]
        a = set(list_s)
        comp_set = sorted(a,reverse=True)
        for i in range(len(comp_set)-1):
            tmp_len = comp_set[i]-comp_set[i+1]
            length.append(tmp_len)
            if tmp_len >100 and tmp_len <500:
                num += 1
                coverage +=tmp_len
        if coverage > tmp_coverage:
            tmp_coverage = coverage
            candidate = key+ ' with ' + key2
        if num > count:
            count = num
            candidate_num = key+' with ' + key2
	keysave[key]=cut[key]
    del cut[key]
length = []
num = 0
coverage = 0            
key,a,key2 = candidate.split()
list_s = keysave[key]+keysave[key2]
a = set(list_s)
comp_set = sorted(a,reverse=True)
for i in range(len(comp_set)-1):
    tmp_len = comp_set[i]-comp_set[i+1]
    length.append(tmp_len)
    if tmp_len >100 and tmp_len <500:
        num += 1
        coverage +=tmp_len
plt.hist(length, rwidth=0.8)
plt.title(key +' with '+key2 +'\n' + str(float(coverage)/len(genome))+' with '+num)
plt.savefig('%s/%s + %s_best_coverage.png'%(save,key,key2))
plt.close()

length = []
num = 0
coverage = 0
key,a,key2 = candidate_num.split()
list_s = keysave[key]+keysave[key2]
a = set(list_s)
comp_set = sorted(a,reverse=True)
for i in range(len(comp_set)-1):
    tmp_len = comp_set[i]-comp_set[i+1]
    length.append(tmp_len)
    if tmp_len >100 and tmp_len <500:
        num += 1
        coverage +=tmp_len
plt.hist(length, rwidth=0.8)
plt.title(key +' with '+key2 +'\n' + str(float(coverage)/len(genome))+' with '+num)
plt.savefig('%s/%s + %s_best_num.png'%(save,key,key2))
plt.close()

with open('best.txt','w') as f:
    f.write(candidate+'\n'+candidate_num)
f_genome.close()
f_enz.close()
