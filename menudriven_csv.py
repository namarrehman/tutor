print('update-->1')
print('delete-->2')
print('exit---->4')

def dell(str1):
        rownum=input('enter the row numer to be deleted')
        del str1[int(rownum)-1]
        return str1

def save(str1):
        print('aa',str1)
        fo=open("book.csv","w+")
        fo.seek(0,0)
        for i in range(0,len(str1)):
                fo.write("%s"%str1[i])

        
j=1
x=input('enter the menu option')
str1=[]
fo=open("book.csv","r+")
for line in fo:
        str1.append(line)
fo.close()
if(int(x)==2):
        str1=dell(str1)
        save(str1)

