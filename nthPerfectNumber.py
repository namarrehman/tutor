'''
nthPerfectNumber(n) 
Write the function nthPerfectNumber(n) that takes a non-negative integer n and returns the nth perfect number, starting at n=0, where a number is perfect if it is the sum of its positive divisors less than itself. For example, 6 is perfect because 6 = 1 + 2 + 3. Also, 28 is perfect because 28 = 1 + 2 + 4 + 7 + 14. The next one is 496, then 8128. For full credit, you need to use a faster version, which uses the same observation that sped up isPrime, so that you only have to search for factors up to the square root of n. 

''''
def nthPerfectNumber(n):
    sum=0
    for i in  range(2,n+1):
        if(n/i-int(n/i)==0.0):
            sum=sum+int(n/i)
            #print(sum)
    if(sum==n):
        print('perfect',n)
        
    
for  j in range(1,100000):
    nthPerfectNumber(j)
