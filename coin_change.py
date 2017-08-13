
"""
Solve coin change with dynamic programming

"""


def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount=cents
        newCoin=1
        for j in [c for c in coinvalueList if c<=cents]:
            if minCoins[cents-j]+1<coinCount:
                coinCount=minCoins[cents-j]+1
                newCoin=j
        minCoins[cents]=coinCount
        coinsUsed[cents]=newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin=change
    while coin>0:
        thisCoin=coinUsed[coin]
        print(thisCoin)
        coin=coin-thisCoin
