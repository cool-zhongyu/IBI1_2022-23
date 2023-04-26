import blosum as bl
xfile=open('ACE2_mouse.fa','r')
yfile=open('ACE2_human.fa','r')
zfile=open('ACE2_cat.fa','r')
matrix=bl.BLOSUM(62)
for line in xfile:
    if not line.startswith('>'):
        seq_m=line.strip()
for line in yfile:
    if not line.startswith('>'):
        seq_h=line.strip()
for line in zfile:
    if not line.startswith('>'):
        seq_c=line.strip()
val1=0
val2=0
val3=0
it1=0
it2=0
it3=0
i=0
while i <len(seq_m):
    m=seq_m[i]
    h=seq_h[i]
    c=seq_c[i]
    val1 +=matrix[m][h]
    val2 +=matrix[m][c]
    val3 +=matrix[c][h]
    i +=1
    if m==h:
        it1 +=1
    if m==c:
        it2 +=1
    if h==c:
        it3 +=1
it1=it1/len(seq_m)
it2=it2/len(seq_h)
it3=it3/len(seq_c)
print('human-mouse','\n',seq_m,'\n',seq_h,'\n',val1,it1)
print('mouse-cat','\n',seq_m,'\n',seq_c,'\n',val2,it2)
print('human-cat','\n',seq_h,'\n',seq_c,'\n',val3,it3)
