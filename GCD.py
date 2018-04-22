'''
gcd(m, n) 
[Note: to receive any credit, you must solve this problem using Euclid's algorithm, and by no other means. In particular, do not just loop through all integers less than min(m,n) and find the common factors that way -- it is much too slow!]
According to Euclid, the greatest common divisor, or gcd, can be found like so:
gcd(x,y) == gcd(y, x%y) 
'''
def gcd(x,y):
    if(y==0):
        print('common diviosr is',x)
        
    else:
        print('x',x,'y',y)
        gcd(y,x%y)

(gcd(270,250))
