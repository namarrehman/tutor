r1=220
r2=189
midpoint=5
diff=(r1-r2)/(midpoint+1)
# print(diff)
for i in range(midpoint):
    r2=r1-((i+1)*diff)
    print((r2,round(r2)))
    