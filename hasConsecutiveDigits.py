'''
hasConsecutiveDigits(n) 
Write the function hasConsecutiveDigits(n) that takes a possibly- negative int value n and returns True if that number contains two consecutive digits that are the same, and False otherwise.
'''

def hasConsecutiveDigits(n):
    f=0
    while(n>0):
        reminder=int(n)%10
        print('reminder',reminder)
        n=int(n)/10
        print('number',int(n))
        if(reminder==int(n)%10):
            f=1
            print(f)
    if(f==1):
        return True
    
print(hasConsecutiveDigits(1234))