'''
threeLinesArea(m1, b1, m2, b2, m3, b3) [30 pts] 
Write the function threeLinesArea(m1, b1, m2, b2, m3, b3) that takes six int or float values representing the 3 lines:
    y = m1*x + b1
    y = m2*x + b2
    y = m3*x + b3
First find where each pair of lines intersects, then return the area of the triangle formed by connecting these three points of intersection. If no such triangle exists (if any two of the lines are parallel), return 0.

To do this, you must write three helper functions: one to find where two lines intersect (which you will call three times), a second to find the distance between two points (perhaps already covered in the notes or in class), and a third to find the area of a triangle given its side lengths (which you will call once). You may write other helper functions if you think they would be useful, but you must at least write these three exactly as described below, and then you must use them appropriately in your solution.

The first required helper function is:
lineIntersection(m1, b1, m2, b2)
This function takes four int or float values representing two lines and returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

The second required helper function is:
distance(x1, y1, x2, y2)
This function takes four int or float values representing two points and returns the distance between those points.

The third required helper function is:
triangleArea(s1, s2, s3)
This function takes three int or float values representing side lengths of a triangle, and returns the area of that triangle. To do this, you may wish to to use Heron's Formula.

Once you have written and tested your helper functions, then move on to writing your threeLinesArea function, which of course should use your helper functions. That's the whole point of helper functions. They help! They help in several ways. First, they are logically simpler -- they break down your logic into smaller chunks that are easier to reason over. Second, they are independently testable, so you can more easily isolate and fix bugs. And third, they are reusable, so you can use them as helper functions for other functions in the future. All good things! 

refernce link
https://www.desmos.com/calculator/lbiu8ice6g
'''
def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1=lineIntersection(m1, b1, m2, b2)
    y1=(m1*x1)+b1
    print('X1',x1)
    print('Y1',y1)
    x2=(lineIntersection(m1, b1, m3, b3))
    y2=(m3*x2)+b3
    print('X2',x2)
    print('Y2',y2)
    distance(x1, y1, x2, y2)
    x3=(lineIntersection(m2, b2, m3, b3))
    y3=(m3*x3)+b3
    print('X3',x3)
    print('Y3',y3)
    s1=distance(x1, y1, x2, y2)
    s2=distance(x1, y1, x3, y3)
    s3=distance(x2, y2, x3, y3)
    print(s1)
    print(s2)
    print(s3)
    triangleArea(s1, s2, s3)
    
    
def triangleArea(s1, s2, s3):
    S=(s1+s2+s3)/2
    area=math.sqrt(S*(S-s1)*(S-s2)*(S-s3))
    print('traingle area',area)
    
def lineIntersection(m1, b1, m2, b2):
    if(m1!=m2):
        x=(b2-b1)/(m1-m2)
        return x
    else:
        return None
def distance(x1, y1, x2, y2):
    s=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    return s

m1=2
b1=1
m2=1
b2=-1
m3=-1
b3=50
threeLinesArea(m1, b1, m2, b2, m3, b3)