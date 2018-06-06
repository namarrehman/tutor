import os
def update(str1):
        dic={}
        str4=[]
        str3=''
        rownum=input("enter the row number(from 1 onwards):")
        columnname=input("enter the cloumn name:")
        fvalue=input("enter the field value:")
        x=str1[int(rownum)].strip('\n').split(",")
        columns=(str1[0]).strip('\n').split(",")#to identify column header
        if columnname in columns:
                for i in range(0,len(columns)):
                        dic["%s"%columns[i]]=x[i]
                dic[columnname]=fvalue
                for i in dic.values():#this used to make the each fields in comma seprated way(join function line #17) ..
                    str4.append(i)
                str3=",".join(str4)+'\n'
                str1[int(rownum)]=str3
        else:
                print('-------invlaid column name----')
        return str1
        
def dell(str1):
        rownum=input('enter the row numer to be deleted')
        del str1[int(rownum)]
        return str1

def save(str1):
        fo=open("book.csv","w")
        for i in range(0,len(str1)):
                fo.write("%s"%str1[i])
        fo.close
if os.path.isfile('book.csv'):
        fo=open("book.csv","r")
        str1=[]
        for line in fo:
                
                str1.append(line)
        while(1):
                print('update-->1')
                print('delete-->2')
                print('exit---->3')
                print('file connetns' ,str1)
                x=input('enter the menu option')
                
                if(int(x)==3):
                        break
                else:
                        if(int(x)==2):
                                str1=dell(str1)
                                print(str1)
                                save(str1)

                        if(int(x)==1):
                                str1=update(str1)
                                print(str1)
                                save(str1)

else:
        print("file doesnt exist")
                
