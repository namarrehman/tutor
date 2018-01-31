import sys

import random



limit = 0;
if (len(sys.argv) == 2):
    limit = int(sys.argv[1])

limit = max(30, limit)
offset = 1000

#I downloaded the file from
#http://deron.meranda.us/data/census-derived-all-first.txt
fp = open('/home/nr83/data/namelist/names.txt')
names = []
i = 0
for line in fp:
    words = line.split()
    if len(words):
        names.append(words[0])


records = []
for i in range(0, limit):
    studid = "{:000005d}".format(i+offset)
    fname = random.choice(names)
    lname = random.choice(names)
    myear = random.choice(range(2010,2018))
    numofcourses = random.choice(range(2,10))
    age = random.choice(range(18,25))
    gpa = random.uniform(1.5, 4)
    gpa = "{:2f}".format(gpa)
    records.append([studid, lname,fname,str(myear),str(gpa),str(numofcourses)])
	
random.shuffle(records)
for i in range(0, limit):
    print('ins', ' '.join(records[i]))


i =  random.choice(range(0, limit))

print('print')

for i in range(limit//10, limit//6):
    print('find', records[i][0])

print('sfind', records[limit//8][0])

for i in range(limit//10, limit//6):
    print('del', records[i][0])

for i in range(limit//10, limit//6):
    print('find', records[i][0])

print('print')

for i in range(limit//10, limit//6):
    range_beg = random.choice(range(0,limit))
    print('range', range_beg, min (range_beg + 10, limit))

for i in range(limit//10, limit//6):
    print('gpa', records[i][0])
    range_beg = random.choice(range(0,limit))
    print('gpa', range_beg, min (range_beg + 100, limit))


for i in range(limit//10, limit//6):
    print('ins', ' '.join(records[i]))


for i in range(limit//10, limit//6):
    print('find', records[i][0])


