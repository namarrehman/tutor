# http://www.krivers.net/15112-f17/notes/lab1.html
'''
colorBlender(rgb1, rgb2, midpoints, n)
 This problem implements a color blender, inspired by this tool. In particular, we will use it with 
 integer RGB values (it also does hex values and RGB% values, but we will not use those modes).
  Note that RGB values contain 3 integers, each between 0 and 255, representing the amount of red, green, and blue respectively in the given color, where 255 is "entirely on" and 0 is "entirely off".
 
For example, consider this case. Here, we are combining crimson (rgb(220, 20, 60)) and mint
 (rgb(189, 252, 201)), using 3 midpoints, to produce this palette (using our own numbering
  convention for the colors, starting from 0, as the tool does not number them): ◦color #0: rgb(220,20,60)
 ◦color #1: rgb(212,78,95)
 ◦color #2: rgb(205,136,131)
 ◦color #3: rgb(197,194,166)
 ◦color #4: rgb(189,252,201)
'''
 
def zeropadding(str1):
    if(len(str(str1))<3):
        str1='0'+str(str1)
        zeropadding(str1)
    else:
        return(str1)

def colorBlender(rgb1,rgb2,mid,n):
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
    print('r1',r1)
    print('g1:',g1)
    print('b1:',b1)
    print('r2:',r2)
    print('g2:',g2)
    print('b2:',b2)
    
    if(r1>r2):
        print(round((r1-r2)/(mid+1)))
        rf=r1-round((r1-r2)/(mid+1))
        print('rf',rf)
    else:
        print(round((r2-r1)/(mid+1)))
        rf=r1+round((r2-r1)/(mid+1))
    if(g1>g2):
        print(round((g1-g2)/(mid+1)))
        gf=r1-round((g1-g2)/(mid+1))
        print('gf',gf)
    else:
        print(round((g2-g1)/(mid+1)))
        gf=g1+round((g2-g1)/(mid+1))
        print('gf',gf)
    
    if(b1>b2):
        print(round((b1-b2)/(mid+1)))
        bf=r1-round((b1-b2)/(mid+1))
        print('bf',bf)
    else:
        print(round((b2-b1)/(mid+1)))
        bf=b1+round((b2-b1)/(mid+1))
        print('bf',bf)
        
    if(n==1):
        print('rf',rf)
        print('gf',gf)
        print('bf',bf)
    else:
            
        rgb1=zeropadding(str(rf))
        # +zeropadding(gf)+zeropadding(bf)
        print('rgb com',rgb1)
        colorBlender(rgb1,rgb2,mid,n-1)

colorBlender(220020060, 189252201, 3,1)