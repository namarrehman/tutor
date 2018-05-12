'''
longestDigitRun(n)
Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns the digit that has the longest consecutive run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (because there is a run of 3 consecutive 7's), as does longestDigitRun(-677886). 
'''

def fn(n1,d):
    x=1
    count=0
    n2=d
    while(n1!=0):
        if(n1%10==d and (n1//10)%10==d):
            count=count+1
            
        n1=int(n1/10)
    return count

n=122322233333
n3=n
i=1
counter=0

while(n3!=0):
    d=n3%10
    count=fn(n,d)
   
    if(counter==count):
        ident=min(ident,d)
    if(counter<count ):
        counter=count
        ident=d
    
    n3=int(n3/10)
    
print ('identified number',ident)
    
