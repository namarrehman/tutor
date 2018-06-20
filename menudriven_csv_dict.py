import os
def update(dicstr1):
        dic={}
        str4=[]
        str3=''
        rownum=input("enter the row number(from 1 onwards):")
        if(int(rownum)<len(dicstr1)):
                columnname=input("enter the cloumn name:")
                if 'columnname' in dic.keys():
                        fvalue=input("enter the field value:")
                        x=dicstr1[int(rownum)]
                        x["%s"%columnname]=fvalue
                        dicstr1[int(rownum)]=x
                else:
                        print('-------invlaid column name----')

        else:
                print('invalid row number')
        return dicstr1
        
def dell(dicstr1):
        rownum=input('enter the row numer to be deleted from 0 onwards')
        del dicstr1[int(rownum)]
        return dicstr1

def save(dicstr1):
        fo=open("book.csv","w")
        col=(','.join(dicstr1[0].keys()))+"\n"
        fo.write(col)
        for i in range(0,len(str1)):
                rec=(','.join(dicstr1[i].values()))+"\n"
                fo.write(rec)
        fo.close

#Program exuection point

if os.path.isfile('book.csv'):
        fo=open("book.csv","r")
        coulmns=((fo.readline().strip("\n"))).split(",")
        dicstr1=[]
        records=[]
        for line in fo:
                dic={}
                records=line.strip('\n').split(',')
                for i in range(0,len(records)):
                        dic["%s"%coulmns[i]]=records[i]
                dicstr1.append(dic)
        #print(dicstr1)
                        
        while(1):
                
                print('update-->1')
                print('delete-->2')
                print('exit---->3')
                print('file connetns' ,dicstr1)
                x=input('enter the menu option')
                
                if(int(x)==3):
                        break
                else:
                        if(int(x)==2):
                                str1=dell(dicstr1)
                                #print(dicstr1)
                                save(str1)

                        if(int(x)==1):
                                str1=update(dicstr1)
                                #print(dicstr1)
                                save(dicstr1)

else:
        print("file doesnt exist")
                
