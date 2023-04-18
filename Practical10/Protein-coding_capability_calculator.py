def cal(DNA_seq):
    seq=DNA_seq.upper()
    import re
    codseqL=re.findall('ATG[ATGC]*TGA',seq)
    codseq=''.join(codseqL)
    codlen=len(codseq)
    seqlen=len(seq)
    seqlen1=seqlen/2
    seqlen2=seqlen/10
    if codlen>seqlen1:
        return 'The sequence is protein-coding.'
    elif codlen<seqlen2:
        return 'The sequence is non-coding.'
    else:
        return 'The sequence is unclear.'
print(cal('aacacacaccacACCACACGAGACGAGCGATGacgTGACGaga'))
