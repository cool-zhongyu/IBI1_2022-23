xfile=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
con=input('The stop codon is:')
dict={}
if con=='TGA':
    output=open('TGA_gene.fa','w')
    for line in xfile:
        if line.startswith('>'):
            name = ''.join(line.split()[0:1])
            dict[name] = ''
        else:
            dict[name] += line.replace('\n', '')
    for key in list(dict.keys()):
        if not dict[key].endswith('TGA'):
            del dict[key]
            continue
    for key in list(dict.keys()):
        seq = dict[key]
        start = seq.count('ATG')
        if start < 1:
            count = 'There is no start condon in the DNA sequence'
        else:
            import re
            sub1 = re.findall('ATG[ATGC]*?$', seq)
            sub = ''.join(sub1)
            num1 = sub.count('TGA')
            key_new=key+'     The coding sequence is: '+str(num1)
            dict[key_new]=dict[key]+str(num1)
            del dict[key]
    print(dict,file=output)
    output.close()
elif con=='TAA':
    output = open('TAA_gene.fa', 'w')
    for line in xfile:
        if line.startswith('>'):
            name = ''.join(line.split()[0:1])
            dict[name] = ''
        else:
            dict[name] += line.replace('\n', '')
    for key in list(dict.keys()):
        if not dict[key].endswith('TAA'):
            del dict[key]
            continue
    for key in list(dict.keys()):
        seq=dict[key]
        start=seq.count('ATG')
        if start < 1:
            count='There is no start condon in the DNA sequence'
        else:
            import re
            sub1 = re.findall('ATG[ATGC]*?$', seq)
            sub = ''.join(sub1)
            num2 = sub.count('TAA')
            key_new=key+'     The coding sequence is: '+str(num2)
            dict[key_new]=dict[key]
            del dict[key]
    print(dict, file=output)
    output.close()
elif con=='TAG':
    output = open('TAG_gene.fa', 'w')
    for line in xfile:
        if line.startswith('>'):
            name = ''.join(line.split()[0:1])
            dict[name] = ''
        else:
            dict[name] += line.replace('\n', '')
    for key in list(dict.keys()):
        if not dict[key].endswith('TAG'):
            del dict[key]
            continue
    for key in list(dict.keys()):
        seq=dict[key]
        start=seq.count('ATG')
        if start < 1:
            count='There is no start condon in the DNA sequence'
        else:
            import re
            sub1 = re.findall('ATG[ATGC]*?$', seq)
            sub = ''.join(sub1)
            num3 = sub.count('TAG')
            key_new=key+'     The coding sequence is: '+str(num3)
            dict[key_new]=dict[key]
            del dict[key]
    print(dict, file=output)
    output.close()
else:
    print('The codon is not one of three codons.')
