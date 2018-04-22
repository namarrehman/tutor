'''
ttp://www.krivers.net/15112-f17/notes/week2-practice.html
4th question
'''''


def Counting_Primes2(n):
#to check each number is prime or not
    count=0
    for k in range(1,n+1):
        if((n/k)-int(n/k)==0.0):
            count=count+1
    return count
    
  
    
def Counting_Primes1(m):
#To get the total count of identified prime numbers 
    a=0
    for i in range(1,m):
        x=Counting_Primes2(i)
        if(x==2):
            print('numbber,count',i,a)
            a=a+1
    return a
    
    
print(Counting_Primes1(100))
