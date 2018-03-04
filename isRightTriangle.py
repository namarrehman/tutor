''''
isRightTriangle(x1, y1, x2, y2, x3, y3) [25 pts]
Write the function isRightTriangle(x1, y1, x2, y2, x3, y3) that takes 
6 int or float values that represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is a right triangle and False otherwise.
You may wish to write a helper function, distance(x1, y1, x2, y2), which you might call several times. Also, remember to use almostEqual (instead of ==) when comparing floats.
'''
import math

def isRightTriangle(x1,y1,x2,y2,x3,y3):
    #Varaibles pq,pr,qr are used to find length of each sides
    pq=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    print(pq)
    pr=math.sqrt(math.pow((x3-x1),2)+math.pow((y3-y1),2))
    print(pr)
    qr=math.sqrt(math.pow((x2-x3),2)+math.pow((y2-y3),2))
    print(qr)
    c=0
    a=0
    b=0
    if(pq<=pr<=qr):#Used for finding the largest side
        c=qr
        a=pr
        b=pq
    if(qr<=pq<=pr):
        c=pr
        a=pq
        b=qr
    if(pr<=qr<=pq):
        c=pq
        a=qr
        b=pr
    if( round(math.pow(c,2))==round((math.pow(a,2)) + round(math.pow(b,2)))):
        print("right traingle")
    else:
        print("not right triangle")
        


#isRightTriangle(-7,4,6,-2,0,15)

isRightTriangle(-2,-3,2,1,5,-2)