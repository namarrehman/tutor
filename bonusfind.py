1'''
http://www.krivers.net/15112-f17/notes/hw1.html
Question number 5

Bonus/optional: bonusFindIntRootsOfCubic(a,b,c,d) [3 pts] 
Write the function bonusFindIntRootsOfCubic(a,b,c,d) that takes the int or float coefficients a, b, c, d of a cubic equation of this form:
      y = ax3 + bx2 + cx + d
 You are guaranteed the function has 3 real roots, and in fact that the roots are all integers.  Your function should return these 3 roots in increasing order.  How does a function return multiple values?  Like so:
     return root1, root2, root3
 To get started, you'll want to read about Cardano's cubic formula here (great stuff!).  Then, from that page, use this formula:
'''