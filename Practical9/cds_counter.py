seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
start=seq.count('ATG')
if start<1:
    print('There is no start condon in the DNA sequence')
else:
    import re
    sub1=re.findall('ATG[ATGC]*?$',seq)
    sub=''.join(sub1)
    num1=sub.count('TGA')
    num2=sub.count('TAA')
    num3=sub.count('TAG')
    num=num1+num2+num3
    print(num)
