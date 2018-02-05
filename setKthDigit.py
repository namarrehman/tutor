
'''Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d -- 
where n is a possibly-negative int, 
k is a non-negative int, and d is a non-negative single digit (between 0 and 9 inclusive), and returns the number n 
but with the kth digit replaced with d. Counting starts at 0 and goes right-to-left, so the 0th digit is the rightmost digit. For example

'''
def fn(base,numb,pos,repl,multi):
    if(pos==0):
        x=numb%10
        y=base-(x*multi)+(repl*multi)
        print(y)
    else:
        fn(base,int(numb/10),pos-1,repl,multi*10)

base=input("enter the number:")
numb=base
pos=input("enter the position:")
repl=input("enter the replacement value between 0 and 9:")
multi=1#multiplication factor

fn(int(base),int(numb),int(pos),int(repl),multi)