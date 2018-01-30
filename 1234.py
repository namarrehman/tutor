print(5/3)  
print("aaa")

#namar=  input("enter your namefs")
#print("namar")

#n=int(input("enter a number"))
#print("half of this number",n/2)
#import math
#print(math.factorial(20))
#print(dir(math))
#import webbrowser
'''
input("hit to enter ")
webbrowser.open("https://docs.python.org/3/library/math.html")

z=5
def fn(x,y):
    print(x+y+z)
    return
fn(1,2)
fn(3,4)

def ispos(x):
    return(x>0)
print(ispos(4))
print(ispos(-1))
def f(w):
    return(10*w)
def g(x,
print(1,end='  ')
print(2)

def cubed(x):
    print(x**3)
    
cubed(2)
print(cubed(5))
print(2*cubed(4))

x=True
y=False
print(x and y)
print(x or y)
print(not y)


def ispostibe(x):
    return(x>0)
print(ispostibe(1))
print(ispostibe(-1))


def f(w):
    return 10*w

def g(x, y):
    return f(3*x) + y

def h(z):
    return f(g(z, f(z+1)))

print(h(1)) # hint: try the "visualize" feature

def one(x):
    return x%10
    
    

def one1(x,y):
    print(max(one(x),one(y)))
    
one1(132,674)   

def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    return f(x*2) + f(x*3)

print(g(2))
 
    
def f(x):
    print("In f, x =", x)
    x += 7
    return round(x / 3)

def g(x):
    x *= 10
    return 2 * f(x)

def h(x):
    x += 3
    return f(x+4) + g(x)

print(h(f(1)))

def f():
    print("user defined ")
    #return 42

import math
print(type(2))
print(type(2.2))
print(type("2.2"))
print(type(2<2.2))

print(type(math))
print(type(math.tan))
print(type(f))

print(type(range(5)))
    
    
print(3 + "def")

def modu(a,b):
    return(a-(a//b)*b)  

print(modu(32,-9))

d1=0.1+0.1+0.1
d2=0.3
print(d1==d2)

e=10**-10
print (e)

def yes():
    return True
def no():
    return False
def crash():
    
    return 1/0
print(yes() or crash())
print(crash())

def iseven(x):
    if(x%2==0):
        print("even")
        elif(x%2
        print("odd")
        
iseven(5)

def isnumber(x):
    return((type(x)==int) or (type(x)==float))



print(isnumber(11))
    
import numbers
def isnumber(x):
    return(isinstance(x,numbers.Number))
    
print(isnumber("ddff"))

def ifstat(x):
    if(x==1):
        print("hello")
    print("dd")
    
ifstat(2)
    
def abs1(n):
    if(n<0):
        n=-n
    return n

print("llll",abs1(-1))


def abs2(n):
    if(n<0):
        return -n
        
    return n

print(abs2(-2))


n=-2
print((n<1)*-n+(n>=1)*n)

print((n<1)*-n)
print((n>=1)*n)


a=1
if(a==1):
    print("a",a)
else:
    
    print("b",b)
    
#-----------------------------
#Write the function nearestOdd(n) that takes an int or float n, and returns as an int value the nearest odd number to n. In the case of a tie, return the smaller odd value. 
def nearestodd(n):
    x=round(n)
    if(x%2==0):
        return x-1
    else:
        return x

print(nearestodd(2.6))
#------------------------------------
##perfect square using for loop
n=100
i=1

for j in range(1,120):
    for i in range(1,j+1):
        if(j/i==i):
            print("perfect",j)

    #else:
     #   print("non perfect",n)
    

#-------------------------------------------perfect sqaure using function


def perfe(x,i):
    if(x/i==i):
        print("perfect")
        return
    else:
        if(i<x):
            perfe(x,i+1)
        else:
            print("not perfect")

        

perfe(5,1)

#....Write the function getKthDigit(n, k) that takes a possibly-negative int n and a non-negative int k, and returns the kth digit of n, starting from 0, counting #from the right. So

def kthdig(n):
    n=(int(n/100000)%10)
    print (n)

kthdig(1234)


def kthdig1(x,n):
    if(n==0):
        print(abs(x)%10)
    else:
        kthdig1(int(abs(x/10)),n-1)
        
kthdig1(-1234,3)


'''

def func1(x,digit):
    if(digit>1):
        x=int(x/10)
        print("inside if...",x)
        print("digit",digit)
        digit=digit-1
        func1(x,digit)
    else:
        print("before mode",x)
        x=x%10
        print("else ",x)
        return 5
'''
def mult(x,y):
    if(x<1):
        y=y*10
        x=x-1
        mult(x,y)
    else:
        return y
'''
main=468
print(func1(main,3))
#y1=mult(3,1)     
#print(main-(x1*y1)+(2*y1))

#print("out",x1)
'''




'''
    


