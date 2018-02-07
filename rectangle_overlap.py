'''rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2)
A rectangle can be described by its left, top, width,
and height. This function takes two rectangles described
this way, and returns True if the rectangles overlap at all
(even if just at a point), and False otherwise.
Note: here we will represent coordinates the
way they are usually represented in computer graphics, where (0,0)
is at the left-top corner of the screen, and while the
x-coordinate goes up while you head right, the y-coordinate goes up while you head down.
Yes, up is down! This is quite common in computer graphics, and is how Tkinter and Brython in particular both work.
Check out the examples in the test code we provided to see this in action.
Up is down. Weird, but true
'''
def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    #below said equuation are used for finding smallest cordinates
    X1=min(x1,x2)
    Y1=min(y1,y2)
    W1=min(w1,w2)
    H1=min(h1,h2)
    X2=max(x1,x2)
    Y2=max(y1,y2)
    W2=max(w1,w2)
    H2=min(h1,h2)
    
    print("X1",X1)
    print("Y1",Y1)
    print("W1",W1)
    print("H1",H1)
    print("X2",X2)
    print("Y2",Y2)
    print("W2",W2)
    print("H2",H2)
    print(int(X1)+int(W1))
    print(int(X1+W1))
    print(int(Y1+H1))
    if(int(X1)+int(W1)>=int(X2) and int(Y1)+int(H1)>=int(Y2)):
        print("both the graphs will oevrlap")
    else:
        print("both the graphs  will not overlap")
        
 
x1=input("enter the value for x1")
y1=input("enter the value for y1")
w1=input("enter the value for w1")
h1=input("enter the value for h1")
x2=input("enter the value for x2")
y2=input("enter the value for y2")
w2=input("enter the value for w2")
h2=input("enter the value for h2")   

rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2)
