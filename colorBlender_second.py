
def findpoint(r1,r2,mid,n):#function to get the next color value
    r1=r1
    r2=r2
    midpoint=mid
    if(n<0 or n>=mid+1):# if value to be found  "n" is greter than the midpoints value(inclusive of first and the 
                        # last value)
        return '-n outside range-'
    diff=((r1-r2))/(midpoint+1)

    for i in range(n+2):
        r2=r1-((i*diff))
        
    return(int(r2+0.5))
        

def colorBlender(rgb1,rgb2,mid,n):
    #line # 18 to 29 is used to find the RGB values of each numbers sets given
    num1=rgb1
    num2=rgb2
    nums1=str(num1)
    r1=int(nums1[0:3])
    g1=int(nums1[3:6])
    b1=int(nums1[6:9])
    nums2=str(num2)
    r2=int(nums2[0:3])
    g2=int(nums2[3:6])
    b2=int(nums2[6:9])
   
    print('number',n,findpoint(r1,r2,mid,n-1),findpoint(g1,g2,mid,n-1),findpoint(b1,b2,mid,n-1))
    
colorBlender(220020060, 189252201,3,4)