print('update-->3')
print('delete-->2')
name=[]
clas=[]
mark=[]
str2=[]
i=0

def update(str1):
        str3=''
        rownum=input("enter the row number(from 1 onwards):")
        field=input("enter the cloumn name:")
        fvalue=input("enter the filed value:")
        fo=open("book.csv","r")
        for line in fo:
            str2.append(line)
        x=str2[int(rownum)].split(",")
        if(field=='name'):
            column=0
        if(field=='class'):
            column=1
        if(field=='mark'):
            column=2
        if (column==len(x)-1):
           x[column]=fvalue+'\n'
        else:
           x[column]=fvalue
        for i in range(0,len(x)):
                if(i==len(x)-1):
                         str3=str3+x[i]
                else:
                        str3=str3+x[i]+','
        str1[int(rownum)]=str3
        return str1
        
def dell(str1):
        rownum=input('enter the row numer to be deleted')
        del str1[int(rownum)]
        return str1

def save(str1):
        fo=open("book.csv","w+")
        fo.seek(0,0)
        for i in range(0,len(str1)):
                fo.write("%s"%str1[i])

        
j=1
filecont=[]
fo=open("book.csv","r")
for line in fo:
        filecont.append(line)
print('file contents',filecont)
fo.close
x=input('enter the menu option')
fo.close
str1=[]
str2=[]
fo=open("book.csv","r+")
for line in fo:
        str1.append(line)
fo.close()
if(int(x)==2):
        str1=dell(str1)
        save(str1)

if(int(x)==3):
        str2=update(str1)
        save(str2)
fo=open("book.csv","r")
filecont=[]
for line in fo:
        filecont.append(line)
print('filecontens',filecont)
fo.close
x=input("enter any key to exit")
