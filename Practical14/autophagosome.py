from xml.dom.minidom import parse
import xml.dom.minidom
import xlwt
f=xlwt.Workbook()
sheet1=f.add_sheet('sheet1')
DOMtree=xml.dom.minidom.parse("go_obo.xml")
obo=DOMtree.documentElement
terms=obo.getElementsByTagName("term")
dic1={}
for term in terms:
    id=term.getElementsByTagName('id')[0].childNodes[0].data
    list1=[]
    for i in term.getElementsByTagName('is_a'):
        list1.append(i.childNodes[0].data)
    for is_a in list1:
        if is_a in dic1:
            dic1[is_a].append(id)
        else:
            dic1[is_a]=[id]
def calculate(list2):
    for i in list2:
        if i in list2:
            if i not in list3:
                list3.append(i)
            if i in dic1:
                calculate(dic1[i])
    return len(list3)
list_is_a=[]
list_id=[]
list_name=[]
list_defstr=[]
for term in terms:
    defstr=term.getElementsByTagName("defstr")[0]
    defstrtxt=defstr.childNodes[0].data
    val=defstrtxt.find('autophagosome')
    if val>=0:
        id=term.getElementsByTagName("id")[0].childNodes[0].data
        name=term.getElementsByTagName("name")[0].childNodes[0].data
        list_id.append(id)
        list_name.append(name)
        list_defstr.append(defstrtxt)
        nodes=0
        list3=[]
        if id in dic1:
           nodes = calculate(dic1[id])
        list_is_a.append(nodes)
for i in range(len(list_id)):
    sheet1.write(i, 0,list_id[i])
    sheet1.write(i, 1,list_name[i])
    sheet1.write(i, 2,list_defstr[i])
    sheet1.write(i, 3, list_is_a[i])
f.save('autophagosome.xls')