xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open('TGA_gene.fa','w')
dict={}
for line in xfile:
    if line.startswith('>'):
        name=''.join(line.split()[0:1])
        dict[name]='\n'
    else:
        dict[name] += line.replace('\n','')
for key in list(dict.keys()):
    if not dict[key].endswith('TGA'):
        del dict[key]
for key in dict:
    dict[key]=dict[key].strip('')
    print(key, dict[key],file=output)
output.close()

