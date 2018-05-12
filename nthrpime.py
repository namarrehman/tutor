'''
Write the function nthAdditivePrime(n) that takes a non-negative int n and returns the nth Additive Prime, which is a prime number such that the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 is also prime, so 113 is an Additive Prime. 
''''


def primecheck(n):
# to check the number is prime or not
    count=0
    for k in range(1,n+1):
        if((n/k)-int(n/k)==0.0):
            count=count+1
    return count
    
  
    
def nthrpime(m):
#
    i=2
    pos=0
    while(1):
        primeyn=primecheck(i)
        if(primeyn==2):#if count is 2 then it has 2 devisibles
            pos=pos+1
        if(pos==m):
            print(i)
            break
        i=i+1


for it in range(1,25):
    nthrpime(it)