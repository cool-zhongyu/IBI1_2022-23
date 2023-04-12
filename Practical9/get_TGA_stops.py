xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open('TGA_gene.fa','w')
dict={}
for line in xfile:
    if line.startswith('>'):
        name=''.join(line.split()[0:1])
        dict[name]=''
    else:
        dict[name] += line.replace('\n','')
for key in list(dict.keys()):
    if not dict[key].endswith('TGA'):
        del dict[key]
        continue
print(dict,file=output)
output.close()
