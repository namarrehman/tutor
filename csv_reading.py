
str=[]
i=1
x=[]
fo=open("book1.csv","r")
for line in fo:
    str.append(line)
print('file content',str)
print('\n')
while(len(str)-1>=i):
    x=str[i].split(",")
    print('num:',x[0])
    
    print('firstname:',x[1])
    print('mark:',x[2])
    i=i+1
