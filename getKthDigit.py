#-----------------------------------------------------------------
#.Write the function getKthDigit(n, k) that takes a possibly-negative int n and a non-negative int k, and returns the kth digit of n, starting from 0, counting #from the right. So



#------------------------------------------------------------------------------------------
def func1(x,digit):
    if(digit>1):
        x=int(x/10)
        #print("inside if...",x)
        # print("digit",digit)
        digit=digit-1
        func1(x,digit)
    else:
        x=x%10
        print(x)
    
def mult(x,y):
    if(x<1):
        y=y*10
        x=x-1
        mult(x,y)
    else:
        return y

main=468
func1(main,3)


