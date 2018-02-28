'''
Hot dogs are an American tradition. Each year, Americans eat up to 20 Billion hot dogs. 
A classic hot dog is made up of two components: 
A frank (the meat) and a bun. Yet, for reasons that mystify mankind, the franks are typically 
sold in packs of ten and the buns in packs of eight. And, of course, you must buy full packages. 
Write the function hotdogPurchase(numHotdogs) that takes the total number of hot dogs you want to make, 
and returns the number of packages of franks and the number of packages of buns you need to purchase.
 You may assume that the argument, numHotdogs, is a non-negative int and the function returns as ints the smallest number of packages of franks and buns that must be purchased
'''
import math

def hotdogPurchase(numHotdogs):
    franks=numHotdogs/10
    bun=numHotdogs/8
    print('number of franks and  buns to be pucrchsed  are', math.ceil(franks),'franks and',math.ceil(bun),'buns')
    #print('kkkk',math.ceil(franks),math.ceil(bun))
numHotdogs = input('enter the number of hotdogs required')
hotdogPurchase(int(numHotdogs))