'''
hotdogExcess(numHotdogs) [25 pts]
Write the function hotdogExcess(numHotdogs) that takes the total number of hot dogs you want to make (as a non-negative integer) and returns the number of excess franks and buns you will need to purchase. Hint: you may want to use hotDogPurchase, which you just wrote!
'''
import math

def hotdogExcess(numHotdogs):
    excess_franks=(math.ceil(franks)*10)-numHotdogs
    excess_bun=(math.ceil(bun)*8)-numHotdogs
    print('excess franks and buns are',excess_franks,excess_bun)
    
def hotdogPurchase(numHotdogs):
    global franks
    global bun
    franks=numHotdogs/10
    bun=numHotdogs/8
    print('number of franks and  buns to be pucrchsed  are', math.ceil(franks),'franks and',math.ceil(bun),'buns')
    #print('kkkk',math.ceil(franks),math.ceil(bun))
    hotdogExcess(numHotdogs)

numHotdogs = input('enter the number of hotdogs required')
hotdogPurchase(int(numHotdogs))
