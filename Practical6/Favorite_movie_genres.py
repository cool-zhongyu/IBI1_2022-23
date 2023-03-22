my_dict={}
# give the variables numbers
com=73
act=42
rom=38
fan=28
sci=22
hor=19
cri=18
doc=12
his=8
war=7
# make a dictionary
genres={'Comedy':com,'Action':act,'Romance':rom,'Fantasy':fan,'Science-fiction':sci}
#add entries
genres['Horror']=hor
genres['Crime']=cri
genres['Documentary']=doc
genres['History']=his
genres['War']=war
# make pie charts
import matplotlib.pyplot as plt
labels='Comedy','Action','Romance','Fantasy','Sciencie-fiction','Horror','Crime','Documentary','History','War'
sizes=[com,act,rom,fan,sci,hor,cri,doc,his,war]

fig,ax=plt.subplots()
ax.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.show()
